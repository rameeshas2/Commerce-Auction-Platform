from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms

from .models import User, Category, Listing, Bid, Comment, Watchlist, SubCategory

from .forms import ListingForm, BidForm, CommentForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q


# def index(request):
#     listings = Listing.objects.filter(active=True)  # Assuming 'active' is a BooleanField
#     print("Listings:", listings)
#     return render(request, "auctions/index.html", {
#         "listings": listings
#     })

def index(request):
    listings = Listing.objects.all()
    categories = Category.objects.prefetch_related('subcategories').all()

    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": categories
    })
    
def search(request):
    query = request.GET.get("q", "").strip()
    results = []

    if query:
        results = Listing.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            active=True  # optional: only show active listings
        )

    return render(request, "auctions/search.html", {
        "query": query,
        "results": results
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.active = True
            listing.save()
            return redirect("index")
    else:
        form = ListingForm()
    return render(request, "auctions/create.html", {
        "form": form,
        "subcategories": SubCategory.objects.all()
    })


def listing(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        return HttpResponse("Listing not found.")

    bids = listing.bids.all().order_by('-amount')
    comments = listing.comments.all().order_by('-timestamp')
    
    highest_bid = bids.first() if bids.exists() else None

    is_owner = request.user == listing.owner

    is_winner = (
        request.user.is_authenticated and
        not listing.active and
        highest_bid and
        highest_bid.bidder == request.user
    )

    in_watchlist = False
    if request.user.is_authenticated:
        in_watchlist = Watchlist.objects.filter(user=request.user, listing=listing).exists()

    return render(request, "auctions/listing.html", {
        "listing": listing,
        "bids": bids,
        "bids_count": bids.count(),
        "comments": comments,
        "bid_form": BidForm(),
        "comment_form": CommentForm(),
        "highest_bid": highest_bid,
        "is_owner": is_owner,
        "is_winner": is_winner,
        "in_watchlist": in_watchlist
    })

@login_required
def add_to_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == "POST" or request.method == "GET":
        Watchlist.objects.get_or_create(user=request.user, listing=listing)
    return redirect("listing", listing_id=listing_id)


@login_required
def remove_from_watchlist(request, listing_id):
    try:
        listing = Listing.objects.get(pk = listing_id)
    except Listing.DoesNotExist:
        return HttpResponse("Listing not found.")

    Watchlist.objects.filter(user = request.user, listing = listing).delete()
    return redirect("listing", listing_id=listing_id)

@login_required
def watchlist_view(request):
    items = Watchlist.objects.filter(user = request.user)
    return render(request, "auctions/watchlist.html", {
        "items": items  # previously was "items"
    })


@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            current_highest = listing.bids.order_by('-amount').first()
            minimum_bid = listing.starting_bid if not current_highest else current_highest.amount

            if amount <= minimum_bid:
                messages.error(request, "Your bid must be higher than the current highest bid.")
            else:
                Bid.objects.create(
                    listing=listing,
                    bidder=request.user,
                    amount=amount
                )
                messages.success(request, "Bid placed successfully.")

    return redirect("listing", listing_id=listing_id)

@login_required
def add_comment(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.listing = listing
            comment.commenter = request.user
            comment.save()
    return redirect("listing", listing_id=listing.id)

@login_required
def close_auction(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.user != listing.owner:
        messages.error(request, "You are not allowed to close this Auction.")
        return redirect("listing", listing_id=listing_id)

    listing.active = False
    listing.save()
    messages.success(request, "Auction Closed!")
    return redirect("listing", listing_id=listing_id)

# views.py

def category_view(request):
    categories = Category.objects.all()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category_listings(request, category_name):
    # First, try to get it as a SubCategory
    try:
        subcategory = SubCategory.objects.get(name=category_name)
        listings = Listing.objects.filter(subcategory=subcategory, active=True)

        return render(request, "auctions/category_listing.html", {
            "listings": listings,
            "category": subcategory,  # For template compatibility
            "parent_category": subcategory.category,
        })

    except SubCategory.DoesNotExist:
        # If not a SubCategory, treat it as a main Category
        category = get_object_or_404(Category, name=category_name)
        listings = Listing.objects.filter(subcategory__category=category, active=True)

        return render(request, "auctions/category_listing.html", {
            "listings": listings,
            "category": category,  # Now it's the main category
            "parent_category": None,
        })
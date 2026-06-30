from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} > {self.name}"

        # return self.name


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    starting_bid = models.DecimalField(max_digits = 10, decimal_places=2)
    image_url = models.URLField(blank = True)
    category = models.ForeignKey  (Category, on_delete = models.CASCADE, blank = True, null = True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.owner.username} - ${self.starting_bid}"
    
    def current_price(self):
        highest_bid = self.bids.order_by('-amount').first()
        return highest_bid.amount if highest_bid else self.starting_bid

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete = models.CASCADE, related_name = 'bids')
    bidder  = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.DecimalField(max_digits = 10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):  
        return f"{self.amount} on {self.listing.title} by {self.bidder.username} at {self.timestamp}"

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.username} on {self.listing.title}: {self.content[:30]}..."

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='watchlist_items')

    def __str__(self):
        return f"{self.user.username} - {self.listing.title}"
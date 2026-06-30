# 🛒 Commerce — Online Auction Platform

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium)

An eBay-inspired online auction platform built with **Django** as part of **CS50's Web Programming with Python and JavaScript (Project 2: Commerce)**. The application allows users to create auction listings, place bids, manage personal watchlists, browse categories, search listings, and participate in online auctions through a modern, responsive interface.

---

# 📌 Project Overview

Commerce is a full-stack web application powered by Django and SQLite that simulates an online auction marketplace similar to eBay. Registered users can create listings, upload images, place bids, save listings to a watchlist, browse products by category, search listings, and manage auctions.

The application demonstrates relational database design, Django authentication, CRUD operations, server-side rendering, and form validation.

---

# ✨ Features

### 👤 User Authentication

- User Registration
- Login
- Logout
- Authentication-protected actions

---

### 🛍️ Auction Listings

- Create auction listings
- Upload product images
- Add title and description
- Set starting bid
- Select category and subcategory
- View active listings

---

### 💰 Bidding System

- Place bids on active auctions
- Bid validation
- Highest bid tracking
- Prevent invalid bids
- Display current winning bid

---

### ⭐ Personal Watchlist

- Add listings to watchlist
- Remove listings
- View saved auctions

---

### 💬 Comments

- Comment on auction listings
- View discussions under each listing

---

### 🔍 Search

- Search listings by keywords
- Display matching auction results

---

### 📂 Categories

- Browse auction categories
- Browse subcategories
- View filtered listings

---

### 🔒 Auction Management

Listing owners can:

- Close auctions
- Stop further bidding
- Display auction winner

---

# 🛠️ Technologies Used

- Python 3
- Django
- SQLite3
- Django ORM
- HTML5
- CSS3
- Bootstrap
- JavaScript
- Selenium WebDriver
- Pytest

---

# 📂 Project Structure

```text
Commerce-Auction-Platform/
│
├── auctions/
│   ├── migrations/
│   ├── static/
│   │   └── auctions/
│   │       ├── auction_logo.png
│   │       ├── styles.css
│   │       └── Shopicons_Regular_Search.png
│   │
│   ├── templates/
│   │   └── auctions/
│   │       ├── layout.html
│   │       ├── index.html
│   │       ├── listing.html
│   │       ├── create.html
│   │       ├── categories.html
│   │       ├── category_listing.html
│   │       ├── watchlist.html
│   │       ├── search.html
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── apps.py
│
├── commerce/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
│   └── subcategory_images/
│
├── tests/
│   ├── test_login.py
│   ├── test_create_listing.py
│   ├── test_bidding.py
│   ├── test_watchlist.py
│   └── conftest.py
│
├── db.sqlite3
├── manage.py
├── .gitignore
└── README.md
```

---

# 🗄️ Database Models

The application uses Django ORM with relational database models including:

- **User**
- **Listing**
- **Category**
- **Subcategory**
- **Bid**
- **Comment**
- **Watchlist**

Relationships include:

- One-to-Many
- Foreign Keys
- Many-to-Many

---

# ⚙️ Application Workflow

```text
Register/Login
        │
        ▼
Browse Listings
        │
        ▼
Search or Filter by Category
        │
        ▼
View Listing Details
        │
        ▼
Place Bid
        │
        ▼
Comment
        │
        ▼
Add to Watchlist
        │
        ▼
Auction Closed
        │
        ▼
Winner Declared
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/your-username/Commerce-Auction-Platform.git
```

---

## Navigate to Project

```bash
cd Commerce-Auction-Platform
```

---

## Install Dependencies

```bash
pip install django
```

---

## Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

## Start Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 📄 Pages

### 🏠 Home

Displays all active auction listings.

---

### 🛍️ Listing Details

- Product information
- Current bid
- Bid form
- Comments
- Watchlist button

---

### ➕ Create Listing

Allows authenticated users to create new auction listings.

---

### ⭐ Watchlist

Displays all saved listings for the logged-in user.

---

### 📂 Categories

Browse listings grouped by categories and subcategories.

---

### 🔍 Search

Search auction listings by keywords.

---

### 👤 Authentication

- Login
- Register
- Logout

---

# 🧪 Automated Testing

The project includes automated end-to-end testing using **Selenium WebDriver** and **Pytest** to verify the functionality of key features through browser-based interactions.

### Test Coverage

- ✅ User Registration & Login
- ✅ Create Auction Listing
- ✅ Bidding Validation
- ✅ Watchlist Management
- ✅ Form Validation
- ✅ User Navigation & Authentication

### Test Files

```text
tests/
├── conftest.py
├── test_login.py
├── test_create_listing.py
├── test_bidding.py
└── test_watchlist.py
```

### Running the Tests

Install the testing dependencies:

```bash
pip install selenium pytest webdriver-manager
```

Run all tests:

```bash
pytest
```

Or execute an individual test:

```bash
pytest tests/test_login.py
pytest tests/test_create_listing.py
pytest tests/test_bidding.py
pytest tests/test_watchlist.py
```

The automated tests simulate real user interactions within a web browser to verify application behavior, ensuring that authentication, bidding, listing creation, and watchlist functionality work as expected.


## Home Page

<img width="1918" height="884" alt="image" src="https://github.com/user-attachments/assets/d8418ff0-f85d-49d3-b596-591a16e2fa6d" />


## Listing Page

<img width="1360" height="870" alt="image" src="https://github.com/user-attachments/assets/87df41a1-cd9f-4a6d-a763-8c6939ef92ea" />


## Watchlist

<img width="1884" height="872" alt="image" src="https://github.com/user-attachments/assets/98ef4ffd-b192-464f-848d-b1a43ccd179d" />


## Categories

<img width="1902" height="871" alt="image" src="https://github.com/user-attachments/assets/32b26947-7ada-4842-8260-a72020843787" />

```

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Django Framework
- Django ORM
- SQLite Database
- User Authentication & Authorization
- CRUD Operations
- Relational Database Design
- Model Relationships
- Form Handling & Validation
- Search & Category Filtering
- Responsive Web Design
- End-to-End Testing with Selenium WebDriver
- Automated Testing using Pytest
---

# 🎓 Course Information

**Course:** CS50's Web Programming with Python and JavaScript

**Project:** Project 2 – Commerce

---

# 👩‍💻 Author

**Rameesha Shahid**

Software Engineering Student

**Areas of Interest**

- Artificial Intelligence
- Machine Learning
- Full-Stack Web Development
- UI/UX Design
- Cybersecurity

---

# 🙏 Acknowledgements

Developed as part of **CS50's Web Programming with Python and JavaScript** by Harvard University.

---

# 📄 License

This project is intended for educational purposes as part of the CS50 Web Programming course.

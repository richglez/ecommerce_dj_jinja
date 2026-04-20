# Ecommerce Django

E-commerce project built with Django (MVT architecture) featuring user authentication and shopping cart functionality.

## Tech Stack

- **Django 6.0.4**
- **SQLite** (db.sqlite3)
- Python templates (Jinja2)

## Features

- User authentication (signup, signin, logout)
- Product catalog
- Shopping cart
- Order management
- Inventory tracking
- Payment processing

## Project Structure

```
ecommerce_dj_jinja/
├── cart/          # Shopping cart (Cart, CartItem models)
├── catalog/       # Product catalog view
├── config/       # Django settings and URLs
├── inventory/    # Stock management
├── orders/       # Order (Pedido) model
├── payments/     # Payment processing
├── products/     # Product model
├── templates/    # Shared templates
└── users/        # Authentication views
```

## Routes

| Path       | View              | Description                |
| ---------- | ----------------- | ------------------------- |
| `/`        | catalog.catalog   | Product catalog          |
| `/admin/`  | admin site        | Django admin panel       |
| `/signup/` | users.signup_view | User registration        |
| `/signin/` | users.signin_view | User login              |
| `/logout/` | users.logout_view | User logout             |
| `/cart/`   | cart_views        | User logout             |

## Setup

```bash
# Activate virtual environment
.\venv\Scripts\python manage.py shell

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

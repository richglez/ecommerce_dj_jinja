# Ecommerce Django

E-commerce project built with Django (MVT architecture) featuring user authentication and shopping cart functionality.

## Tech Stack

- **Django 6.0.4**
- **SQLite** (db.sqlite3)
- Python templates (Jinja2)

## Features

- User authentication (signup, signin, logout)
- Product catalog
- Shopping cart (with session support for anonymous users)
- Order management (Pedido, PedidoItem)
- Inventory tracking
- Payment processing

## Project Structure

```
ecommerce_dj_jinja/
├── cart/          # Shopping cart (Cart, CartItem models)
├── catalog/      # Product catalog view
├── config/       # Django settings and URLs
├── inventory/    # Stock management (Inventory model)
├── orders/       # Order management (Pedido, PedidoItem models)
├── payments/     # Payment processing (Payment model)
├── products/     # Product model
├── templates/     # Shared templates
└── users/        # Authentication views
```

## Models

### Product (`products/`)
- `name` - CharField(max_length=200)
- `price` - DecimalField(max_digits=10, decimal_places=2)
- `description` - TextField
- `is_active` - BooleanField

### Cart (`cart/`)
- `user` - OneToOneField(User) - supports authenticated users
- `session_key` - CharField - supports anonymous users via cookies
- `created_at` - DateTimeField

### CartItem (`cart/`)
- `cart` - ForeignKey(Cart)
- `product` - ForeignKey(Product)
- `quantity` - PositiveIntegerField

### Pedido (`orders/`)
- `customer` - ForeignKey(User)
- `date` - DateTimeField
- `total` - DecimalField
- `status` - CharField (pending, processing, shipped, delivered, cancelled)
- `created_at`, `updated_at` - DateTimeField

### PedidoItem (`orders/`)
- `pedido` - ForeignKey(Pedido)
- `product` - ForeignKey(Product)
- `quantity` - PositiveIntegerField
- `price` - DecimalField

### Inventory (`inventory/`)
- `product` - OneToOneField(Product)
- `quantity` - PositiveIntegerField
- `location` - CharField
- `last_updated` - DateTimeField

### Payment (`payments/`)
- `pedido` - ForeignKey(Pedido)
- `user` - ForeignKey(User)
- `stripe_payment_id` - CharField(unique=True)
- `amount` - DecimalField
- `status` - CharField (pending, completed, failed, refunded)
- `created_at`, `updated_at` - DateTimeField

## Routes

| Path       | View              | Description                |
| ---------- | ----------------- | -------------------------- |
| `/`        | catalog.catalog   | Product catalog           |
| `/admin/`  | admin site        | Django admin panel         |
| `/signup/` | users.signup_view | User registration          |
| `/signin/` | users.signin_view | User login                 |
| `/logout/` | users.logout_view | User logout                |

## User Flow

```
┌─────────────────┐
│   Visit Catalog │  (/)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Browse Products│  View products from catalog
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Add to Cart   │  Product → CartItem (quantity)
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌───────┐ ┌───────┐
│Guest  │ │Login  │
│Session│ │User  │
│Cookie │ │Auth  │
└───┬───┘ └───┬───┘
    │         │
    ▼         ▼
┌─────────────────┐
│    View Cart    │  Review items
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Checkout      │  Create Pedido order
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Process Payment│  Stripe integration
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Update Inventory│  Decrement stock
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Order Complete │  Pedido status: pending → processing → shipped → delivered
└─────────────────┘
```

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

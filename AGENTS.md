# AGENTS.md

## Run Commands

```bash
# Activate venv first (required)
.\venv\Scripts\python manage.py <command>

# Common commands
python manage.py runserver      # Start dev server
python manage.py migrate      # Apply migrations
python manage.py makemigrations  # Create migrations
python manage.py createsuperuser
python manage.py shell      # Django shell
```

## Project Structure

- **Django 6.0.4** with 7 apps: cart, users, orders, payments, products, inventory, catalog
- **SQLite** database (`db.sqlite3`)
- **Template dirs**: `templates/` (root)
- **Entry point**: `config/urls.py` → routes to catalog view at `/`

## Routes

| Path | View |
|------|------|
| `/` | catalog.catalog |
| `/admin/` | admin site |
| `/signup/` | users.signup_view |
| `/signin/` | users.signin_view |
| `/logout/` | users.logout_view |

## Known Issues

- **settings.py:126** - `LOGIN_URL` has typo: `/sigin/` should be `/signin/`

## App Ownership

- `products/` - Product model (name, price, description, is_active)
- `orders/` - Pedido model (customer_id FK to User, date, total)
- `inventory/` - inventory tracking
- `payments/` - payment processing
- `cart/` - shopping cart
- `users/` - auth views (signup, signin, logout)
- `catalog/` - product catalog view

## Testing

Each app has `tests.py` with placeholder `from django.test import TestCase`. No test framework configured (pytest not in use).
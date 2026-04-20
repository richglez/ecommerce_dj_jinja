## Ecommerce Django Auth
This is a ecommerce project scalable, using authentication. MVT (Model-View-Template).

# Features


# Tech Stack


## Project Structure
```
└─── src/
     └─── cart/          # User cart (Cart, CartItem, Cart View/Template)
     └─── catalog/       # Public catalog (Catalog View/Template)
     └─── config/        # Gloabl django config (settings.py / urls.py)
     └─── inventory/     # Store inventory (Stock status...)
     └─── orders/        # User orders
     └─── payments/      # User system payments
     └─── products/      # Store list of products (Product)
     └─── templates/     # Global Layouts for all the apps
     └─── users/         # Signin/Signup/Logout Views/Templates
```


## User Routes

| Path       | View              |
| ---------- | ----------------- |
| `/`        | catalog.catalog   |
| `/admin/`  | admin site        |
| `/signup/` | users.signup_view |
| `/signin/` | users.signin_view |
| `/logout/` | users.logout_view |

## Admin routes

- `admin/products/` - Product model (name, price, description, is_active)
- `admin/orders/` - Pedido model (customer_id FK to User, date, total)
- `admin/inventory/` - inventory tracking
- `admin/payments/` - payment processing
- `admin/cart/` - shopping cart
- `admin/users/` - auth views (signup, signin, logout)
- `admin/catalog/` - product catalog view



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


## Routes

| Path       | View              | Permision                                       |
| ---------- | ----------------- | ----------------------------------------------- |
| `/`        | catalog.catalog   | Public (anyone can acces to this url)           |
| `/admin/`  | admin site        | Private needs a superuser staff                 |
| `/signup/` | users.signup_view | Public (anyone can signup)                      |
| `/signin/` | users.signin_view | Public (anyone can signin within account)       |
| `/logout/` | users.logout_view | Private (needs auth)                            |
| `/cart/`   | cart.cart_view    | Public (anyone can acces add a shopping cart)   |

## Admin routes

- `admin/products/` - Product model (name, price, description, is_active)
- `admin/orders/` - Pedido model (customer_id FK to User, date, total)
- `admin/inventory/` - inventory tracking
- `admin/payments/` - payment processing
- `admin/cart/` - shopping cart
- `admin/users/` - auth views (signup, signin, logout)
- `admin/catalog/` - product catalog view



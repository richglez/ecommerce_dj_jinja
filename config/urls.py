from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views as user_views
from catalog import views as catalog_views
from cart import views as cart_views
from inventory import urls as inventory_urls

urlpatterns = [
    path("", include(inventory_urls)),
    path("admin/", admin.site.urls),
    path("signup/", user_views.signup_view, name="signup"),
    path("signin/", user_views.signin_view, name="signin"),
    path("logout/", user_views.logout_view, name="logout"),
    path("cart/", cart_views.cart_view, name="cart"),
    path("cart/add/<int:product_id>/", cart_views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", cart_views.remove_from_cart, name="remove_from_cart"),
    path("cart/update/<int:product_id>/", cart_views.update_cart, name="update_cart"),
    path("", catalog_views.catalog, name="index"),
]

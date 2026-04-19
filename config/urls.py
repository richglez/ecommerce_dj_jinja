from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views as user_views
from catalog import views as catalog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", user_views.signup_view, name="signup"),
    path("signin/", user_views.signin_view, name="signin"),
    path("logout/", user_views.logout_view, name="logout"),
    path("", catalog_views.catalog, name="index"),
]

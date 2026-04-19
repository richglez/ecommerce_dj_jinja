from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views as user_views
from catalog import views as catalog_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", user_views.signup, name="signup"),
    path("", catalog_views.catalog, name="home"),
]

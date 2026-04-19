from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", views.signup),
]

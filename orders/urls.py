from django.urls import path
from orders.views import my_profile
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('accounts/profile/', my_profile),
]

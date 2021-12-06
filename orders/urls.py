from django.urls import path
from orders.views import my_profile
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('accounts/profile/', my_profile),
    path("addpasta/", views.addpasta, name="addpasta"),
    path("addsub/", views.addsub, name="addsub"),
    path("addpizza/", views.addpizza, name="addpizza"),
    path("adddinner/", views.adddinner, name="adddinner"),
    path("addsalad/", views.addsalad, name="addsalad"),
    path("ordenes/", views.ordenes, name="ordenes"),
    path("car/", views.mycar, name="car"),
     
]

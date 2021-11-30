from django import forms
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# from orders.forms import Menu
from orders.models import Pizza
from orders.models import Pasta,Ordenes,detallepasta

# Create your views here.
def index(request):
    # formulario = Menu()
    # if request.method =="GET":
    #     print("GET method")
    # else:
    #     formulario = Menu(request.POST, request.FILES)
    #     if formulario.is_valid():
    #         formulario.save()
    #     else:
    #         print("Algo pasó")
    #         print(request.POST)
    #         cantidad


    #     print("POST method")
    
    context = {
        
        "pasta": Pasta.objects.all() # select * from pizza
    }


    
    return render(request, 'orders/index.html',context)

def my_profile(request):
    return render(request, 'accounts/profile.html')

def getorder(user):
    ordern=Ordenes.objects.filter(estado=1).first()
    if not ordern:
       ordern=Ordenes.objects.create(cliente=user)
    return ordern

def addpasta(request):
    if request.method=="POST":
        orden=getorder(request.user)
        print("---------------------------")
        print(orden)
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_pasta=request.POST.get("pasta")
        print("---------------------------pasta")
        print(id_pasta)
        pasta=Pasta.objects.get(pk=id_pasta)
        print("---------------------------idpasta")
        print(pasta)
        price=pasta.price
        print("----------------price")
        print(price)
        total_pasta=(price*cantidad)
        print("----------------total")
        print(total_pasta)

        detallepasta_O=detallepasta(orden=orden,pasta=pasta,cantidad=cantidad,price=pasta.price)
        print("---------------------------")
        print(detallepasta_O)
        # detallepasta_O.save()
        return redirect("/")
    else:
        context = {
        
        "pasta": Pasta.objects.all() # select * from pizza
    }


    return render(request, 'orders/addpasta.html',context)

def register(request):
    if request.method== "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data["username"]
            messages.success(request,f"usuario {user} registrado")
            return render(request, 'accounts/profile.html')

    else:
        form = UserRegisterForm()

    context = {"form" : form }

    return render(request, 'registration/register.html',context)



from django import forms
from django.db import models
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
# from orders.forms import Menu
from orders.models import Pizza
from orders.models import *

# Create your views here.
def index(request):
   
    context = {
        
        "pasta": Pasta.objects.all() # select * from pizza
    }


    
    return render(request, 'orders/index.html',context)

def my_profile(request):
    return render(request, 'accounts/profile.html')

def getorder(user):
    ordern=Ordenes.objects.filter(estado=1,cliente=user).first()
    if not ordern:
       ordern=Ordenes.objects.create(cliente=user)
    return ordern



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


def addpasta(request):
    if request.method=="POST":
        orden=getorder(request.user)
        
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
        orden.total+=total_pasta
        orden.save()
        detallepasta_O=Detallepasta(orden=orden,pasta=pasta,cantidad=cantidad,price=pasta.price)
        print("---------------------------")
        print(detallepasta_O)
        messages.success(request,f"Agregado al carrito")
        detallepasta_O.save()
        print(detallepasta_O)
        return redirect("/")
    else:
        context = {
        
        "pasta": Pasta.objects.all() # select * from pizza
    }


    return render(request, 'orders/addpasta.html',context)

def addsub(request):
    if request.method=="POST":
        orden=getorder(request.user)
        
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_subs=request.POST.get("sub")
        print("---------------------------pasta")
        print(id_subs)
        sub=Subs.objects.get(pk=id_subs)
        print("---------------------------idpasta")
        print(sub)
        price=sub.price
        print("----------------price")
        print(price)
        total_pasta=(price*cantidad)
        print("----------------total")
        print(total_pasta)
        orden.total+=total_pasta
        orden.save()
        detallesub_O=Detallesub(orden=orden,sub=sub,cantidad=cantidad,price=sub.price)
        print("---------------------------")
        print(detallesub_O)
        detallesub_O.save()
        return redirect("/")
    else:
        context = {
        
        "sub": Subs.objects.all() # select * from sub
    }


    return render(request, 'orders/addsub.html',context)


def adddinner(request):
    if request.method=="POST":
        orden=getorder(request.user)
        # print("---------------------------")
        # print(orden)
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_dinners=request.POST.get("dinner")
        print("---------------------------pasta")
        print(id_dinners)
        dinner=Dinner.objects.get(pk=id_dinners)
        print("---------------------------idpasta")
        print(dinner)
        price=dinner.price
        print("----------------price")
        print(price)
        total_pasta=(price*cantidad)
        print("----------------total")
        print(total_pasta)
        orden.total+=total_pasta
        orden.save()
        detalledinner_O=Detalledinner(orden=orden,dinner=dinner,cantidad=cantidad,price=dinner.price)
        print("---------------------------")
        print(detalledinner_O)
        detalledinner_O.save()
        return redirect("/")
    else:
        context = {
        
        "dinner": Dinner.objects.all() # select * from dinner
    }


    return render(request, 'orders/adddinner.html',context)

def addsalad(request):
    if request.method=="POST":
        orden=getorder(request.user)
        
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_salads=request.POST.get("salad")
        print("---------------------------pasta")
        print(id_salads)
        salad=Salads.objects.get(pk=id_salads)
        print("---------------------------idpasta")
        print(salad)
        price=salad.price
        print("----------------price")
        print(price)
        total_pasta=(price*cantidad)
        print("----------------total")
        print(total_pasta)
        orden.total+=total_pasta
        orden.save()
        detallesalad_O=Detallesalads(orden=orden,salad=salad,cantidad=cantidad,price=salad.price)
        print("---------------------------")
        print(detallesalad_O)
        detallesalad_O.save()
        return redirect("/")
    else:
        context = {
        
        "salad": Salads.objects.all() # select * from salad
    }


    return render(request, 'orders/addsalad.html',context)


def addpizza(request):
    if request.method=="POST":
        orden=getorder(request.user)
        
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_pizza=request.POST.get("pizza")
        pizza=Pizza.objects.get(pk=id_pizza)
        print("---------------------------idpizza")
        print(pizza)
        price=pizza.price
        print("----------------price")
        print(price)
        total_pizza=(price*cantidad)
        print("----------------total")
        print(total_pizza)
        orden.total+=total_pizza
        orden.save()
        detallepizza_O=Detallepizza(orden=orden,pizza=pizza,cantidad=cantidad,price=pizza.price)
        print("---------------------------")
        print(detallepizza_O)
        detallepizza_O.save()
        return redirect("/")
    else:
        context = {
        
        "pizza": Pizza.objects.all(), # select * from pizza
        "topping":Topings.objects.all(),
    }


    return render(request, 'orders/addpizza.html',context)


def ordenes(request):
      
    if request.method=="POST":
        estado=request.POST.get("estado")
        print(estado)
        if estado == "0":
            estado=getorder(request.user)
            estado.estado=0
            estado.save()

        if estado == "2":
            estado=getorder(request.user)
            print("----")
            print(estado)
            estado.estado=2
            estado.save()
            


    context = {
            "ordenes":Ordenes.objects.filter(estado=2),
        
    }

    return render(request,'orders/ordenes.html',context)

def mycar(request):
    #if request.method=="POST":
    orden=getorder(request.user)
    
    
    context={
        "car":orden
    }
    return render(request,'orders/car.html',context)
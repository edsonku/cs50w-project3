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
def georder(user):
    ordern=Ordenes.objects.filter(estado=2).first()
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
        id_pasta=request.POST.get("pasta")
        pasta=Pasta.objects.get(pk=id_pasta)
        price=pasta.price
        total_pasta=(price*cantidad)
        orden.total+=total_pasta
        orden.save()
        detallepasta_O=Detallepasta(orden=orden,pasta=pasta,cantidad=cantidad,price=pasta.price)
        messages.success(request,f"Agregado al carrito")
        detallepasta_O.save()
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
        id_subs=request.POST.get("sub")
        sub=Subs.objects.get(pk=id_subs)
        price=sub.price
        total_pasta=(price*cantidad)
        orden.total+=total_pasta
        orden.save()
        detallesub_O=Detallesub(orden=orden,sub=sub,cantidad=cantidad,price=sub.price)
        messages.success(request,f"Agregado al carrito")
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
        cantidad=int(request.POST.get("cantidad"))
        id_dinners=request.POST.get("dinner")
        dinner=Dinner.objects.get(pk=id_dinners)
        price=dinner.price
        total_pasta=(price*cantidad)
        orden.total+=total_pasta
        orden.save()
        detalledinner_O=Detalledinner(orden=orden,dinner=dinner,cantidad=cantidad,price=dinner.price)
        messages.success(request,f"Agregado al carrito")
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
        id_salads=request.POST.get("salad") 
        salad=Salads.objects.get(pk=id_salads)
        price=salad.price
        total_pasta=(price*cantidad)
        orden.total+=total_pasta
        orden.save()
        detallesalad_O=Detallesalads(orden=orden,salad=salad,cantidad=cantidad,price=salad.price)
        messages.success(request,f"Agregado al carrito")
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
        id_t1=request.POST.get("toping1")
        
        id_t2=request.POST.get("toping2")
        
        id_t3=request.POST.get("toping3")
        
        cantidad=int(request.POST.get("cantidad"))
        print("---------------------------cantidad")
        print(cantidad)
        id_pizza=request.POST.get("pizza")
        pizza=Pizza.objects.get(pk=id_pizza)
        print("---------------------------idpizza")
        print(pizza)
        price=pizza.price
        size=pizza.size
        print("----------------price")
        print(size)
        top=[]
        if size=="1 Topping":
            t1=Topings.objects.get(pk=id_t1)
            print(t1)
            top.append(t1)
        if size=="2 Topping":
            t1=Topings.objects.get(pk=id_t1)
            print(t1)
            t2=Topings.objects.get(pk=id_t2)
            print(t2)
            top.append(t1)
            top.append(t2)
        if size=="3 Topping":
            t1=Topings.objects.get(pk=id_t1)
            print(t1)
            t2=Topings.objects.get(pk=id_t2)
            print(t2)
            t3=Topings.objects.get(pk=id_t3)
            print(t3)
            top.append(t1)
            top.append(t2)
            top.append(t3)

        total_pizza=(price*cantidad)
        print("----------------total")
        print(total_pizza)
        
        orden.total+=total_pizza
        orden.save()
        
        detallepizza_O=Detallepizza(orden=orden,pizza=pizza,cantidad=cantidad,price=pizza.price)
        messages.success(request,f"Agregado al carrito")
        print("---------------------------")
        print(detallepizza_O)
        detallepizza_O.save()

        for i in top:
            detallepizza_O.toppings.add(i)
        
        return redirect("/")
    else:
        context = {
        
        "pizza": Pizza.objects.all(), # select * from pizza
        "topping":Topings.objects.all(),
    }


    return render(request, 'orders/addpizza.html',context)


def ordenes(request):
    state=1
    if request.method=="POST":
        state=1
        state=request.POST.get("estado")
        if state == "0":
            estado=getorder(request.user)
            estado.estado=0
            estado.save()
            

        if state== "2":
            estado=getorder(request.user)
            estado.estado=2
            estado.save()
            
    else:
        state=1
        
        
        # x=Detallepizza.orden.all
        # print(x)

    context = {
            "ordenes":Ordenes.objects.filter(estado=2),
            "car":georder(request.user),
            
        
    }

    return render(request,'orders/ordenes.html',context)

def mycar(request):
    #if request.method=="POST":
    orden=getorder(request.user)
    
    print(orden)
    context={
        "car":orden
    }
    return render(request,'orders/car.html',context)


def detalleorden(request, pk_order):
    orden=Ordenes.objects.get(pk=pk_order)
    
    print(orden)
    context={
       "orden":orden
    }
    
    return render(request,'orders/detalleorden.html',context)

def addmenu(request):
    if request.method=="POST":
        pizza=request.POST.get("pizza")
        price=request.POST.get("price")
        size=request.POST.get("size")

        sub=request.POST.get("sub")
        pricesub=request.POST.get("pricesub")
        sizesub=request.POST.get("sizesub")

        salad=request.POST.get("salad")
        pricesa=request.POST.get("pricesa")
        

        dinner=request.POST.get("dinner")
        priced=request.POST.get("priced")
        sized=request.POST.get("sized")

        pasta=request.POST.get("pasta")
        pricep=request.POST.get("pricep")
        

        print(pizza,price,size)

        if pizza and price and size:
            print("paso")
            detalle_p=Pizza(pizza=pizza,size=size,price=price)
            
            detalle_p.save()
        if sub and pricesub and sizesub:
            print("pasosu")
            detalle_s=Subs(subs=sub,size=sizesub,pricesub=pricesub)
            
            detalle_s.save()
        if pasta and pricep :
            print("pasop")
            detalle_pa=Pizza(Pasta=pasta,price=pricep)
            
            detalle_pa.save()
        if dinner and priced and sized:
            print("pasod")
            detalle_d=Dinner(dinner=dinner,size=sized,price=priced)
            
            detalle_d.save()
        if salad and pricesa :
            print("pasosa")
            detalle_s=Salads(salads=salad,price=pricesa)
            detalle_s.save()
        messages.success(request,f"Agregado al menu")
        return render(request,'orders/addmenu.html')
    return render(request,'orders/addmenu.html')
  
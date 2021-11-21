from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def index(request):
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


    return render(request, 'orders/index.html',context)

def my_profile(request):
    return render(request, 'accounts/profile.html')

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



from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

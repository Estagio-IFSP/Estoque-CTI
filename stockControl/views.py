from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from stockControl.models import ConsumableGood
from stockControl.models import Supplier
from .forms import ConsumableGoodForm
from .forms import SupplierForm

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def password_recovery(request):
    return render(request, "password-recovery.html")

def dashboard(request):
    return render(request, "dashboard.html")

def new_consumable_good(request):
    if request.method == "POST":
        form = ConsumableGoodForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ConsumableGoodForm()

    return render(request, "new_consumable_good.html", { "form": form })

def new_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()

    return render(request, "new_supplier.html", { "form": form })

class ConsumableGoodListView(ListView):
    model = ConsumableGood
    template_name = "consumable_list.html"
    context_object_name = "consumables"

class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

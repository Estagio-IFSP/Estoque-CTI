from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import ListView
from stockControl.models import ConsumableGood
from stockControl.models import PermanentGood
from stockControl.models import Supplier
from stockControl.models import Claimant
from stockControl.models import Loan
from .forms import ConsumableGoodForm
from .forms import PermanentGoodForm
from .forms import SupplierForm
from .forms import ClaimantForm
from .forms import LoanForm

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

def new_permanent_good(request):
    if request.method == "POST":
        form = PermanentGoodForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PermanentGoodForm()

    return render(request, "new_permanent_good.html", { "form": form })

def new_supplier(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierForm()

    return render(request, "new_supplier.html", { "form": form })

def new_claimant(request):
    if request.method == "POST":
        form = ClaimantForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClaimantForm()

    return render(request, "new_claimant.html", { "form": form })

def new_loan(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanForm()

    return render(request, "new_loan.html", { "form": form })

class ConsumableGoodListView(ListView):
    model = ConsumableGood
    template_name = "consumable_good_list.html"
    context_object_name = "consumables"

class PermanentGoodListView(ListView):
    model = PermanentGood
    template_name = "permanent_good_list.html"
    context_object_name = "permanents"

class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

class ClaimantListView(ListView):
    model = Claimant
    template_name = "claimant_list.html"
    context_object_name = "claimants"

class LoanListView(ListView):
    model = Loan
    template_name = "loan_list.html"
    context_object_name = "loans"

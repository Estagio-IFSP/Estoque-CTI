from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import DetailView
from django.views.generic import ListView
from stockControl.models import Supplier
from stockControl.models import Claimant
from stockControl.models import Loan
from stockControl.models import Good
from .forms import GoodForm
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

def new_good(request):
    if request.method == "POST":
        form = GoodForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GoodForm()

    return render(request, "new_good.html", { "form": form })

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

class GoodDetailView(DetailView):
    model = Good
    template_name = "good_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GoodListView(ListView):
    model = Good
    template_name = "good_list.html"
    context_object_name = "goods"

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

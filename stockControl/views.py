from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
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

class GoodUpdateView(UpdateView):
    model = Good
    template_name = "update.html"
    fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier", "permanent", "warranty_expiry_date", "warranty_details" ]
    context_object_name = "goods"

class GoodDeleteView(DeleteView):
    model = Good
    template_name = "delete.html"
    success_url = reverse_lazy("goods")

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "supplier_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "update.html"
    fields = [ "name", "phone_number" ]

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "delete.html"
    success_url = reverse_lazy("supplier")

class ClaimantDetailView(DetailView):
    model = Claimant
    template_name = "claimant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ClaimantListView(ListView):
    model = Claimant
    template_name = "claimant_list.html"
    context_object_name = "claimants"

class ClaimantUpdateView(UpdateView):
    model = Claimant
    template_name = "update.html"
    fields = [ "name", "phone_number" ]

class ClaimantDeleteView(DeleteView):
    model = Claimant
    template_name = "delete.html"
    success_url = reverse_lazy("claimant")

class LoanDetailView(DetailView):
    model = Loan
    template_name = "loan_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class LoanListView(ListView):
    model = Loan
    template_name = "loan_list.html"
    context_object_name = "loans"

class LoanUpdateView(UpdateView):
    model = Loan
    template_name = "update.html"
    fields = [ "good", "quantity", "claimant", "loan_date", "return_date", ]

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = "delete.html"
    success_url = reverse_lazy("loan")


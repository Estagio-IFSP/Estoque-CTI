from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.db.models import ProtectedError
from stockControl.models import Supplier, Claimant, Loan, Good
from .forms import GoodForm, SupplierForm,ClaimantForm, LoanForm

class ProtectedAwareDeleteView(DeleteView):

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        except ProtectedError as error:
            return render(request, "protected-error.html", {"object": self.object, "error": error})

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

class GoodListView(ListView):
    model = Good
    template_name = "good_list.html"
    context_object_name = "goods"

class GoodUpdateView(UpdateView):
    model = Good
    template_name = "update.html"
    fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier", "permanent", "warranty_expiry_date", "warranty_details" ]

class GoodDeleteView(ProtectedAwareDeleteView):
    model = Good
    template_name = "delete.html"
    success_url = reverse_lazy("goods")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        except ProtectedError as error:
            return render(request, "protected-error.html", {"object": self.object, "error": error})

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "supplier_detail.html"

class SupplierListView(ListView):
    model = Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "update.html"
    fields = [ "name", "phone_number" ]

class SupplierDeleteView(ProtectedAwareDeleteView):
    model = Supplier
    template_name = "delete.html"
    success_url = reverse_lazy("suppliers")

class ClaimantDetailView(DetailView):
    model = Claimant
    template_name = "claimant_detail.html"

class ClaimantListView(ListView):
    model = Claimant
    template_name = "claimant_list.html"
    context_object_name = "claimants"

class ClaimantUpdateView(UpdateView):
    model = Claimant
    template_name = "update.html"
    fields = [ "name", "phone_number" ]

class ClaimantDeleteView(ProtectedAwareDeleteView):
    model = Claimant
    template_name = "delete.html"
    success_url = reverse_lazy("claimants")

class LoanDetailView(DetailView):
    model = Loan
    template_name = "loan_detail.html"

class LoanListView(ListView):
    model = Loan
    template_name = "loan_list.html"
    context_object_name = "loans"

class LoanUpdateView(UpdateView):
    model = Loan
    template_name = "update.html"
    fields = [ "good", "quantity", "claimant", "loan_date", "return_date", ]

class LoanDeleteView(ProtectedAwareDeleteView):
    model = Loan
    template_name = "delete.html"
    success_url = reverse_lazy("loans")

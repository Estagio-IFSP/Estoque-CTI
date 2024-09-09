from datetime import date
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.db.models import ProtectedError
from stockControl.models import Good, Supplier, Claimant, Loan, LoanItem
from .forms import GoodForm, SupplierForm,ClaimantForm, LoanForm, LoanItemForm

class ProtectedAwareDeleteView(DeleteView):
    def post(self, request, *args):
        self.object = self.get_object()
        try:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        except ProtectedError as error:
            return render(request, "protected_error.html", {"object": self.object, "error": error})


class RedirectableDetailView(DetailView):
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse(self.model.slug + "-detail", kwargs={"pk": pk})

class RedirectableCreateView(CreateView):
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.fcc_form = form.save(commit=True)
            messages.add_message(self.request, messages.INFO, 'Created')
            return HttpResponseRedirect(reverse(self.model.slug + '-detail', kwargs={'pk': self.fcc_form.pk}))
        else:
            messages.add_message(self.request, messages.ERROR, 'Error')
            return render(request, self.template_name, {'form': form})

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")

def password_recovery(request):
    return render(request, "password_recovery.html")

def dashboard(request):
    return render(request, "dashboard.html")

class GoodCreateView(RedirectableCreateView):
    model = Good
    template_name = "new_good.html"
    form_class = GoodForm
    initial = { "acquisition_date": date.today() }

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
            return render(request, "protected_error.html", {"object": self.object, "error": error})

class SupplierCreateView(RedirectableCreateView):
    model = Supplier
    template_name = "new_supplier.html"
    form_class = SupplierForm

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

class ClaimantCreateView(RedirectableCreateView):
    model = Claimant
    template_name = "new_claimant.html"
    form_class = ClaimantForm
    initial = { "identifier": "JC" }

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

class LoanCreateView(RedirectableCreateView):
    model = Loan
    template_name = "new_loan.html"
    form_class = LoanForm
    initial = { "loan_date": date.today() }

class LoanDetailView(RedirectableDetailView):
    model = Loan
    template_name = "loan_detail.html"

class LoanListView(ListView):
    model = Loan
    template_name = "loan_list.html"
    context_object_name = "loans"

class LoanUpdateView(UpdateView):
    model = Loan
    template_name = "update.html"
    fields = [ "claimant", "loan_date", "return_date", ]


class LoanDeleteView(ProtectedAwareDeleteView):
    model = Loan
    template_name = "delete.html"
    success_url = reverse_lazy("loans")

class LoanItemCreateView(CreateView):
    model = LoanItem
    template_name = "new_loan_item.html"
    form_class = LoanItemForm

    def get_initial(self):
        initial = super().initial.copy()
        self.loan_pk = self.kwargs.get('loan_pk', None)
        initial['loan'] = self.loan_pk
        return initial

    def get_success_url(self):
        return reverse('loan-detail', kwargs={"pk": self.object.loan.pk})

class LoanItemDetailView(DetailView):
    model = LoanItem
    template_name = "loan_item_detail.html"

class LoanItemListView(ListView):
    model = LoanItem
    template_name = "loan_item_list.html"
    context_object_name = "loan_items"

class LoanItemUpdateView(UpdateView):
    model = LoanItem
    template_name = "update.html"
    fields = [ "good", "quantity", ]

class LoanItemDeleteView(ProtectedAwareDeleteView):
    model = LoanItem
    template_name = "delete.html"
    success_url = reverse_lazy("loan-items")

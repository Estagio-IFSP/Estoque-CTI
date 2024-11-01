from datetime import date, timedelta
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.db.models import ProtectedError, Subquery, OuterRef, Q
from stockControl.models import Good, Supplier, Claimant, Loan, LoanItem
from .forms import GoodForm, SupplierForm,ClaimantForm, LoanForm, LoanItemForm, SignUpForm

items_per_page = 15

class ProtectedAwareDeleteView(LoginRequiredMixin, DeleteView):
    def post(self, request, pk, *args):
        self.object = self.get_object()
        try:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        except ProtectedError as error:
            return render(request, "error_protected.html",
                          {"object": self.object, "error": error})

class RedirectableDetailView(LoginRequiredMixin, DetailView):
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse(self.model.slug + "-detail", kwargs={"pk": pk})

class RedirectableCreateView(LoginRequiredMixin, CreateView):
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.fcc_form = form.save(commit=True)
            messages.add_message(self.request, messages.INFO, 'Created')
            return HttpResponseRedirect(reverse(self.model.slug + '-detail',
                                                kwargs={'pk': self.fcc_form.pk}))
        else:
            messages.add_message(self.request, messages.ERROR, 'Error')
            return render(request, self.template_name, {'form': form})

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class DashboardHomeView(LoginRequiredMixin, ListView):
    model = Loan
    paginate_by = itens_per_page
    template_name = "dashboard.html"
    context_object_name = "loans"

class GoodCreateView(RedirectableCreateView):
    model = Good
    template_name = "good_create.html"
    form_class = GoodForm
    initial = { "acquisition_date": date.today() }

class GoodDetailView(LoginRequiredMixin, DetailView):
    model = Good
    template_name = "good_detail.html"

    def get_loans(self):
        loans = Loan.objects.filter(
            id__in=Subquery(
                LoanItem.objects.filter(good=self.get_object())
                .values('loan_id')
                .distinct()
            )
        )
        return loans

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["associated_loans"] = self.get_loans()
        return context

class GoodListView(LoginRequiredMixin, ListView):
    model = Good
    paginate_by = itens_per_page
    template_name = "good_list.html"
    context_object_name = "goods"

class GoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Good
    form_class = GoodForm
    template_name = "good_update.html"

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
            return render(request, "error_protected.html",
                          {"object": self.object, "error": error})

class SupplierCreateView(RedirectableCreateView):
    model = Supplier
    template_name = "supplier_create.html"
    form_class = SupplierForm

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = "supplier_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["supplier_goods"] = Good.objects.filter(supplier=self.get_object())
        return context

class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    paginate_by = itens_per_page
    template_name = "supplier_list.html"
    context_object_name = "suppliers"

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = "update.html"
    fields = [ "name", "phone_number" ]

class SupplierDeleteView(ProtectedAwareDeleteView):
    model = Supplier
    template_name = "delete.html"
    success_url = reverse_lazy("suppliers")

class ClaimantCreateView(RedirectableCreateView):
    model = Claimant
    template_name = "claimant_create.html"
    form_class = ClaimantForm
    initial = { "identifier": "JC" }

class ClaimantDetailView(LoginRequiredMixin, DetailView):
    model = Claimant
    template_name = "claimant_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["claimant_loans"] = Loan.objects.filter(claimant=self.get_object())
        return context


class ClaimantListView(LoginRequiredMixin, ListView):
    model = Claimant
    paginate_by = itens_per_page
    template_name = "claimant_list.html"
    context_object_name = "claimants"

class ClaimantUpdateView(LoginRequiredMixin, UpdateView):
    model = Claimant
    template_name = "update.html"
    fields = [ "identifier", "name", "phone_number", "email" ]

class ClaimantDeleteView(ProtectedAwareDeleteView):
    model = Claimant
    template_name = "delete.html"
    success_url = reverse_lazy("claimants")

class LoanCreateView(RedirectableCreateView):
    model = Loan
    template_name = "loan_create.html"
    form_class = LoanForm
    initial = { "loan_date": date.today(),
               "return_date": date.today() + timedelta(days=30) }

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            self.fcc_form = form.save(commit=True)
            messages.add_message(self.request, messages.INFO, 'Created')
            return HttpResponseRedirect(reverse('loan-add-item',
                                                kwargs={'loan_pk': self.fcc_form.pk}))
        else:
            messages.add_message(self.request, messages.ERROR, 'Error')
            return render(request, self.template_name, {'form': form})

class LoanDetailView(RedirectableDetailView):
    model = Loan
    template_name = "loan_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loan_items"] = LoanItem.objects.filter(loan=self.get_object())
        return context

class LoanListView(LoginRequiredMixin, ListView):
    model = Loan
    paginate_by = itens_per_page
    template_name = "loan_list.html"
    context_object_name = "loans"

class LoanUpdateView(LoginRequiredMixin, UpdateView):
    model = Loan
    template_name = "update.html"
    fields = [ "claimant", "loan_date", "return_date", ]

class LoanDeleteView(ProtectedAwareDeleteView):
    model = Loan
    template_name = "delete.html"
    success_url = reverse_lazy("loans")

class LoanItemCreateView(LoginRequiredMixin, CreateView):
    model = LoanItem
    template_name = "loan_item_create.html"
    form_class = LoanItemForm

    def get_initial(self):
        initial = super().initial.copy()
        self.loan_pk = self.kwargs.get('loan_pk', None)
        initial['loan'] = self.loan_pk
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["loan"] = Loan.objects.get(pk=self.kwargs.get('loan_pk', None))
        context["loan_items"] = LoanItem.objects.filter(
            loan=self.kwargs.get('loan_pk', None)
        )
        return context

    def get_success_url(self):
        return reverse('loan-detail', kwargs={"pk": self.object.loan.pk})

class LoanItemDetailView(LoginRequiredMixin, DetailView):
    model = LoanItem
    template_name = "loan_item_detail.html"

class LoanItemListView(LoginRequiredMixin, ListView):
    model = LoanItem
    paginate_by = itens_per_page
    template_name = "loan_item_list.html"
    context_object_name = "loan_items"

class LoanItemUpdateView(LoginRequiredMixin, UpdateView):
    model = LoanItem
    template_name = "update.html"
    fields = [ "loan", "good", "quantity", "returned", ]

    def get_success_url(self):
        return reverse('loan-detail', kwargs={"pk": self.object.loan.pk})

class LoanItemDeleteView(LoginRequiredMixin, DeleteView):
    model = LoanItem
    template_name = "delete.html"

    def get_success_url(self):
        return reverse('loan-detail', kwargs={"pk": self.object.loan.pk})

    def post(self, request, pk, *args):
        self.object = self.get_object()
        try:
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
        except ProtectedError as error:
            return render(request, "error_protected.html",
                          {"object": self.object, "error": error})

class SearchView(ListView):
    template_name = 'search.html'
    context_object_name = "results"

    def get_queryset(self):
        query = self.request.GET.get("query")

        goods = Good.objects.filter(
            Q(name__unaccent__icontains=query) |
                Q(description__unaccent__icontains=query) |
                Q(warranty_details__unaccent__icontains=query) |
                Q(supplier__name__unaccent__icontains=query)
        )
        loan_items = LoanItem.objects.filter(
            Q(good__name__unaccent__icontains=query) |
            Q(good__description__unaccent__icontains=query) |
            Q(good__warranty_details__unaccent__icontains=query) |
            Q(good__supplier__name__unaccent__icontains=query) |
                Q(loan__claimant__name__unaccent__icontains=query)
        )
        claimants = Claimant.objects.filter(
            Q(name__unaccent__icontains=query) |
                Q(phone_number__unaccent__icontains=query) |
                Q(email__unaccent__icontains=query) |
                Q(identifier__icontains=query)
        )
        suppliers = Supplier.objects.filter(
            Q(name__unaccent__icontains=query) |
                Q(phone_number__unaccent__icontains=query)
        )

        matches = {
            'goods': goods,
            'loan_items': loan_items,
            'claimants': claimants,
            'suppliers': suppliers,
        }

        return matches

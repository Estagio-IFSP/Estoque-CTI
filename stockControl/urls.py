from django.contrib import admin
from django.urls import path
from stockControl.views import login, signup, password_recovery, dashboard
from stockControl.views import GoodDetailView, GoodListView, GoodUpdateView, GoodDeleteView
from stockControl.views import SupplierDetailView, SupplierListView, SupplierUpdateView, SupplierDeleteView
from stockControl.views import ClaimantDetailView, ClaimantListView, ClaimantUpdateView, ClaimantDeleteView
from stockControl.views import LoanDetailView, LoanListView, LoanUpdateView, LoanDeleteView
from stockControl.views import LoanItemDetailView, LoanItemListView, LoanItemUpdateView, LoanItemDeleteView
from stockControl.views import GoodCreateView, ClaimantCreateView, LoanCreateView, SupplierCreateView, LoanItemCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path("signup", signup, name="signup"),
    path("password-recovery", password_recovery, name="password-recovery"),
    path("dashboard", dashboard, name="dashboard"),

    path("dashboard/goods", GoodListView.as_view(), name="goods"),
    path("dashboard/new-good", GoodCreateView.as_view(), name="new-good"),
    path("dashboard/good/<int:pk>/", GoodDetailView.as_view(), name="good-detail"),
    path("dashboard/good/<int:pk>/edit", GoodUpdateView.as_view(), name="good-edit"),
    path("dashboard/good/<int:pk>/delete", GoodDeleteView.as_view(), name="good-delete"),

    path("dashboard/suppliers", SupplierListView.as_view(), name="suppliers"),
    path("dashboard/new-supplier", SupplierCreateView.as_view(), name="new-supplier"),
    path("dashboard/supplier/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("dashboard/supplier/<int:pk>/edit", SupplierUpdateView.as_view(), name="supplier-edit"),
    path("dashboard/supplier/<int:pk>/delete", SupplierDeleteView.as_view(), name="supplier-delete"),

    path("dashboard/claimants", ClaimantListView.as_view(), name="claimants"),
    path("dashboard/new-claimant", ClaimantCreateView.as_view(), name="new-claimant"),
    path("dashboard/claimant/<int:pk>/", ClaimantDetailView.as_view(), name="claimant-detail"),
    path("dashboard/claimant/<int:pk>/edit", ClaimantUpdateView.as_view(), name="claimant-edit"),
    path("dashboard/claimant/<int:pk>/delete", ClaimantDeleteView.as_view(), name="claimant-delete"),

    path("dashboard/loans", LoanListView.as_view(), name="loans"),
    path("dashboard/new-loan", LoanCreateView.as_view(), name="new-loan"),
    path("dashboard/loan/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
    path("dashboard/loan/<int:pk>/edit", LoanUpdateView.as_view(), name="loan-edit"),
    path("dashboard/loan/<int:pk>/delete", LoanDeleteView.as_view(), name="loan-delete"),

    path("dashboard/loan-items", LoanItemListView.as_view(), name="loan-items"),
    path("dashboard/new-loan-item", LoanItemCreateView.as_view(), name="new-loan-item"),
    path("dashboard/loan-item/<int:pk>/", LoanItemDetailView.as_view(), name="loan-item-detail"),
    path("dashboard/loan-item/<int:pk>/edit", LoanItemUpdateView.as_view(), name="loan-item-edit"),
    path("dashboard/loan-item/<int:pk>/delete", LoanItemDeleteView.as_view(), name="loan-item-delete"),
]

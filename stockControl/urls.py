from django.contrib import admin
from django.urls import path
from stockControl.views import login
from stockControl.views import signup
from stockControl.views import password_recovery
from stockControl.views import dashboard
from stockControl.views import GoodDetailView
from stockControl.views import GoodListView
from stockControl.views import SupplierDetailView
from stockControl.views import SupplierListView
from stockControl.views import ClaimantDetailView
from stockControl.views import ClaimantListView
from stockControl.views import LoanDetailView
from stockControl.views import LoanListView
from stockControl.views import new_good
from stockControl.views import new_claimant
from stockControl.views import new_loan
from stockControl.views import new_supplier

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", login, name="login"),
    path("signup", signup, name="signup"),
    path("password-recovery", password_recovery, name="password_recovery"),
    path("dashboard", dashboard, name="dashboard"),

    path("dashboard/goods", GoodListView.as_view(), name="goods"),
    path("dashboard/new_good", new_good, name="new_good"),
    path("dashboard/good/<int:pk>/", GoodDetailView.as_view(), name="good-detail"),

    path("dashboard/suppliers", SupplierListView.as_view(), name="suppliers"),
    path("dashboard/new_supplier", new_supplier, name="new_supplier"),
    path("dashboard/supplier/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),

    path("dashboard/claimants", ClaimantListView.as_view(), name="claimants"),
    path("dashboard/new_claimant", new_claimant, name="new_claimant"),
    path("dashboard/claimant/<int:pk>/", ClaimantDetailView.as_view(), name="claimant-detail"),

    path("dashboard/loans", LoanListView.as_view(), name="loans"),
    path("dashboard/new_loan", new_loan, name="new_loan"),
    path("dashboard/loan/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
]

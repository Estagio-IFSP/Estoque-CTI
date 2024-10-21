from django.conf import settings
from django.urls import path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.static import serve
from stockControl.forms import CustomAuthenticationForm
from stockControl.views import SignUpView, DashboardHomeView
from stockControl.views import GoodDetailView, GoodListView, GoodUpdateView, GoodDeleteView
from stockControl.views import SupplierDetailView, SupplierListView, SupplierUpdateView, SupplierDeleteView
from stockControl.views import ClaimantDetailView, ClaimantListView, ClaimantUpdateView, ClaimantDeleteView
from stockControl.views import LoanDetailView, LoanListView, LoanUpdateView, LoanDeleteView
from stockControl.views import LoanItemDetailView, LoanItemListView, LoanItemUpdateView, LoanItemDeleteView
from stockControl.views import GoodCreateView, ClaimantCreateView, LoanCreateView, SupplierCreateView, LoanItemCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", auth_views.LoginView.as_view(form_class=CustomAuthenticationForm), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("password-change/",
         auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name="password-change"),
    path("password-change-done/",
         auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_confirmation.html"),
         name="password_change_done"),
    path("password-recovery/",
         auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
         name="password-recovery"),
    path("password-reset-done/",
         auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_change.html"),
         name="password_reset_confirm"),
    path("reset/done/",
         auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_change_confirmation.html"),
         name="password_reset_complete"),

    path("dashboard/", DashboardHomeView.as_view(), name="dashboard"),
    path("dashboard/goods/", GoodListView.as_view(), name="goods"),
    path("dashboard/good/create/", GoodCreateView.as_view(), name="good-create"),
    path("dashboard/good/<int:pk>/", GoodDetailView.as_view(), name="good-detail"),
    path("dashboard/good/<int:pk>/edit/", GoodUpdateView.as_view(), name="good-edit"),
    path("dashboard/good/<int:pk>/delete/", GoodDeleteView.as_view(), name="good-delete"),

    path("dashboard/suppliers/", SupplierListView.as_view(), name="suppliers"),
    path("dashboard/supplier/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("dashboard/supplier/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("dashboard/supplier/<int:pk>/edit/", SupplierUpdateView.as_view(), name="supplier-edit"),
    path("dashboard/supplier/<int:pk>/delete/", SupplierDeleteView.as_view(), name="supplier-delete"),

    path("dashboard/claimants/", ClaimantListView.as_view(), name="claimants"),
    path("dashboard/claimant/create/", ClaimantCreateView.as_view(), name="claimant-create"),
    path("dashboard/claimant/<int:pk>/", ClaimantDetailView.as_view(), name="claimant-detail"),
    path("dashboard/claimant/<int:pk>/edit/", ClaimantUpdateView.as_view(), name="claimant-edit"),
    path("dashboard/claimant/<int:pk>/delete/", ClaimantDeleteView.as_view(), name="claimant-delete"),

    path("dashboard/loans/", LoanListView.as_view(), name="loans"),
    path("dashboard/loan/create/", LoanCreateView.as_view(), name="loan-create"),
    path("dashboard/loan/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
    path("dashboard/loan/<int:pk>/edit/", LoanUpdateView.as_view(), name="loan-edit"),
    path("dashboard/loan/<int:pk>/delete/", LoanDeleteView.as_view(), name="loan-delete"),
    path("dashboard/loan/<int:loan_pk>/add-item/", LoanItemCreateView.as_view(), name="loan-add-item"),

    path("dashboard/loan-items/", LoanItemListView.as_view(), name="loan-items"),
    path("dashboard/loan-item/<int:pk>/", LoanItemDetailView.as_view(), name="loan-item-detail"),
    path("dashboard/loan-item/<int:pk>/edit/", LoanItemUpdateView.as_view(), name="loan-item-edit"),
    path("dashboard/loan-item/<int:pk>/delete/", LoanItemDeleteView.as_view(), name="loan-item-delete"),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

from django.contrib import admin
from .models import Good, Claimant, Supplier, Loan, LoanItem

admin.site.register(Good)
admin.site.register(Claimant)
admin.site.register(Supplier)
admin.site.register(Loan)
admin.site.register(LoanItem)

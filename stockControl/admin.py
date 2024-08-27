from django.contrib import admin
from .models import Good, Claimant, Supplier, Loan

admin.site.register(Good)
admin.site.register(Claimant)
admin.site.register(Supplier)
admin.site.register(Loan)

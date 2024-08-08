from django.contrib import admin
from .models import Good, ConsumableGood, PermanentGood, Stock, Supplier, Warranty, Loan

admin.site.register(Good)
admin.site.register(ConsumableGood)
admin.site.register(PermanentGood)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Warranty)
admin.site.register(Loan)

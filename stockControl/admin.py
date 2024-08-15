from django.contrib import admin
from .models import ConsumableGood, PermanentGood, Stock, Supplier, Loan

admin.site.register(ConsumableGood)
admin.site.register(PermanentGood)
admin.site.register(Stock)
admin.site.register(Supplier)
admin.site.register(Loan)

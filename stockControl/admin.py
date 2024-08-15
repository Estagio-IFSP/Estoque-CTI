from django.contrib import admin
from .models import ConsumableGood, PermanentGood, Supplier, Loan

admin.site.register(ConsumableGood)
admin.site.register(PermanentGood)
admin.site.register(Supplier)
admin.site.register(Loan)

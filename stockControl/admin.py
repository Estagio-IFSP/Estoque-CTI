from django.contrib import admin
from .models import ConsumableGood, PermanentGood, Stock, Supplier

admin.site.register(ConsumableGood)
admin.site.register(PermanentGood)
admin.site.register(Stock)
admin.site.register(Supplier)

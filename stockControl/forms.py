from django import forms
from django.forms import ModelForm
from stockControl.models import ConsumableGood
from stockControl.models import Supplier

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ConsumableGoodForm(BaseForm):
    class Meta:
        model = ConsumableGood
        fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier" ]

class SupplierForm(BaseForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone" ]

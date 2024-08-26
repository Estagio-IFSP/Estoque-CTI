from django import forms
from django.forms import CheckboxInput
from stockControl.models import Good
from stockControl.models import Supplier
from stockControl.models import Claimant
from stockControl.models import Loan

# Atribui as classes do Bootstrap a todos os campos dos formulários
class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if type(field.widget) is CheckboxInput:
                field.widget.attrs['class'] = 'form-check'
            else:
                field.widget.attrs['class'] = 'form-control'

class GoodForm(BaseModelForm):
    class Meta:
        model = Good
        fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier", "permanent", "warranty_expiry_date", "warranty_details" ]

class SupplierForm(BaseModelForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone_number" ]

class ClaimantForm(BaseModelForm):
    class Meta:
        model = Claimant
        fields = [ "name", "identifier", "phone_number" ]

class LoanForm(BaseModelForm):
    class Meta:
        model = Loan
        fields = [ "good", "quantity", "claimant", "loan_date", "return_date", ]

from datetime import date
from django import forms
from django.db.models.constraints import ValidationError
from django.forms import CheckboxInput
from stockControl.models import Good, Supplier, Claimant, Loan, LoanItem
from django.forms.fields import IntegerField

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
        fields = [ "name", "quantity", "acquisition_date", "description", "supplier", "permanent", "warranty_expiry_date", "warranty_details" ]

class SupplierForm(BaseModelForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone_number" ]

class ClaimantForm(BaseModelForm):
    class Meta:
        model = Claimant
        fields = [ "name", "identifier", "phone_number" ]
        labels = {
            "identifier": "Identificador (prontuário)",
        }

class LoanForm(BaseModelForm):
    class Meta:
        model = Loan
        fields = [ "claimant", "loan_date", "return_date", ]

class LoanItemForm(BaseModelForm):
    quantity = IntegerField()

    class Meta:
        model = LoanItem
        fields = [ "loan", "good", "quantity", ]

    def clean(self):
        cleaned_data = super().clean()
        cleaned_good = cleaned_data.get("good")
        cleaned_quantity = cleaned_data.get("quantity")

        if cleaned_quantity > cleaned_good.get_available_quantity():
            raise ValidationError("A quantidade solicitada excede quantidade disponível")

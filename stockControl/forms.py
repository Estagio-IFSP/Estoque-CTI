from django import forms
from django.contrib.contenttypes.forms import generic_inlineformset_factory
from stockControl.models import Good
from stockControl.models import ConsumableGood
from stockControl.models import PermanentGood
from stockControl.models import Supplier
from stockControl.models import Claimant
from stockControl.models import Loan

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ConsumableGoodForm(BaseModelForm):
    class Meta:
        model = ConsumableGood
        fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier" ]

class PermanentGoodForm(BaseModelForm):
    class Meta:
        model = PermanentGood
        fields = [ "name", "quantity", "acquisition_date", "description", "status", "supplier", "patrimony", "warranty_expiry_date", "warranty_details" ]

class SupplierForm(BaseModelForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone" ]

class ClaimantForm(BaseModelForm):
    class Meta:
        model = Claimant
        fields = [ "identifier", "phone_number" ]

class LoanForm(BaseModelForm):
    class Meta:
        model = Loan
        fields = [ "loan_date", "return_date", "quantity", "claimant" ] # "good",

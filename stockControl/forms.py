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
        labels = {
            "name": "Nome",
            "quantity": "Quantidade",
            "phone_number": "Telefone",
            "acquisition_date": "Data de aquisição",
            "description": "Descrição",
            "supplier": "Fornecedor",
            "permanent": "Permanente",
            "warranty_expiry_date": "Data de expiração da garantia",
            "warranty_details": "Detalhes da garantia",
        }

class SupplierForm(BaseModelForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone_number" ]
        labels = { "name": "Nome", "phone_number": "Telefone" }

class ClaimantForm(BaseModelForm):
    class Meta:
        model = Claimant
        fields = [ "name", "identifier", "phone_number" ]
        labels = {
            "name": "Nome",
            "identifier": "Identificador (prontuário)",
            "phone_number": "Telefone"
        }

class LoanForm(BaseModelForm):
    class Meta:
        model = Loan
        fields = [ "good", "quantity", "claimant", "loan_date", "return_date", ]
        labels = {
            "good": "Bem",
            "quantity": "Quantidade",
            "claimant": "Requerente",
            "loan_date": "Data do empréstimo",
            "return_date": "Data de devolução",
        }

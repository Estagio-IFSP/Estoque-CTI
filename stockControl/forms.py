from datetime import date
from django import forms
from django.db.models.constraints import ValidationError
from django.forms import CheckboxInput
from stockControl.models import Good, Supplier, Claimant, Loan, LoanItem
from django.forms.fields import IntegerField
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User

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

    def clean(self):
        cleaned_data = super().clean()
        permanent = cleaned_data.get("permanent")
        warranty_details = cleaned_data.get("warranty_details")
        warranty_expiry_date = cleaned_data.get("warranty_expiry_date")

        if permanent and not (warranty_details and warranty_expiry_date):
            raise ValidationError("Bens permanentes requerem dados de garantia.")

class SupplierForm(BaseModelForm):
    class Meta:
        model = Supplier
        fields = [ "name", "phone_number" ]

class ClaimantForm(BaseModelForm):
    class Meta:
        model = Claimant
        fields = [ "name", "identifier", "email", "phone_number", ]
        labels = {
            "identifier": "Identificador (prontuário)",
        }

class LoanForm(BaseModelForm):
    class Meta:
        model = Loan
        fields = [ "claimant", "loan_date", "return_date", ]

class LoanItemForm(BaseModelForm):
    class Meta:
        model = LoanItem
        fields = [ "loan", "good", "quantity", ]

    def format_unavailable_quantity_error(self, available, good):
        if available == 0:
            return "Não há unidades disponíveis de {}".format(good)
        elif available == 1:
            return "Há apenas uma unidade disponível de {}".format(good)
        else:
            return "Há apenas {} unidades disponíveis de {}".format(available, good)

    def clean(self):
        cleaned_data = super().clean()
        good = cleaned_data.get("good")
        requested_quantity = cleaned_data.get("quantity")
        available_quantity = good.get_available_quantity()

        if requested_quantity > available_quantity:
            raise ValidationError(self.format_unavailable_quantity_error(available_quantity, good))

class SignUpForm(BaseUserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")
        field_classes = {"username": UsernameField}
        labels = {
            "username": "Prontuário",
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
            "autofocus"
        ] = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CustomAuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label = 'Prontuário',
        widget = forms.TextInput(attrs={"autofocus": True}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # if self._meta.model.USERNAME_FIELD in self.fields:
        #     self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
        #     "autofocus"
        # ] = True
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

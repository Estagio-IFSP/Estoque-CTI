from django.forms import ModelForm
from stockControl.models import ConsumableGood

class ConsumableGoodForm(ModelForm):
    class Meta:
        model = ConsumableGood
        fields = ["name", "description", "status", "quantity"]


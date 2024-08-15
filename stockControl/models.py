from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

# Bem (permanente e de consumo
class Good(models.Model):
    good_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    type_id = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    quantity = models.PositiveBigIntegerField()
    acquisition_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    class Meta:
        abstract = True

# Bem de consumo
class ConsumableGood(Good):
    pass

# Bem permanente
class PermanentGood(Good):
    patrimony = models.BooleanField()
    warranty_expiry_date = models.DateField()
    warranty_details = models.TextField();

# Requerente (Pessoa que empresta um bem)
class Claimant(models.Model):
    identifier = models.CharField()
    phone_number = models.PositiveIntegerField()

# Empréstimo
class Loan(models.Model):
    good = GenericForeignKey("good_type", "type_id")
    good_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    type_id = models.PositiveIntegerField()
    loan_date = models.DateField()
    return_date = models.DateField()
    quantity = models.PositiveBigIntegerField()
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT)

from django.db import models


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

# Garantia
class Warranty(models.Model):
    expiryDate = models.DateField()
    details = models.TextField();

# Bem (permanente e de consumo
class Good(models.Model):
    name = models.CharField(max_length=100)
    acquisitionDate = models.DateField()
    quantity = models.PositiveBigIntegerField()
    description = models.TextField()
    status = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier, on_delete = models.PROTECT)

# Bem de consumo
class ConsumableGood(Good):
    pass

# Bem permanente
class PermanentGood(Good):
    patrimony = models.BooleanField()
    warranty = models.ManyToManyField(Warranty)

# Pessoa que empresta um bem
class Claimant(models.Model):
    identifier = models.CharField()
    phone_number = models.PositiveIntegerField()

# Empréstimo
class Loan(models.Model):
    good = models.ForeignKey(Good, on_delete = models.PROTECT)
    loanDate = models.DateField()
    returnDate = models.DateField()
    quantity = models.PositiveBigIntegerField()
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT)

# Estoque
class Stock(models.Model):
    quantity = models.PositiveBigIntegerField()
    category = models.CharField(max_length=50)
    actionDate = models.DateField()

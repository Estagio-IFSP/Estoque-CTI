from django.db import models

# Bens permanentes e de consumo
class ConsumableGood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=30)
    quantidade = models.PositiveBigIntegerField()

class PermanentGood(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=30)
    loanDate = models.DateField()
    claimant = models.CharField(max_length=50)

# Estoque
class Stock(models.Model):
    quantity = models.PositiveBigIntegerField()
    category = models.CharField(max_length=50)
    actionDate = models.DateField()

#Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)



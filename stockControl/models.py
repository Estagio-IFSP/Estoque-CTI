from django.db import models
from django.urls import reverse
from datetime import date


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    slug = "supplier"
    localized_class_name = "Fornecedor"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Bem (permanente e de consumo)
class Good(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.PositiveBigIntegerField()
    acquisition_date = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=30)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    permanent = models.BooleanField()
    warranty_expiry_date = models.DateField()
    warranty_details = models.TextField();
    slug = "good"
    localized_class_name = "Bem"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Requerente (Pessoa que empresta um bem)
class Claimant(models.Model):
    name = models.CharField()
    identifier = models.CharField(unique=True)
    phone_number = models.PositiveIntegerField()
    slug="claimant"
    localized_class_name = "Requerente"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Empréstimo
class Loan(models.Model):
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT)
    loan_date = models.DateField()
    return_date = models.DateField()
    slug = "loan"
    localized_class_name = "Empréstimo"

    def __str__(self):
        return "Empréstimo por " + str(self.claimant.name) + " em " + str(self.loan_date)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

    def due_check(self):
        return date.today() > self.return_date

# Item de empréstimo
class LoanItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.PROTECT)
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    slug = 'loan-item'

    def __str__(self):
        return "Item de Empréstimo " + str(self.good.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

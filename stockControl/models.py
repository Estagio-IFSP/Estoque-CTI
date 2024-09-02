from django.db import models
from django.urls import reverse
from datetime import date


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    slug = "supplier"
    localized_class_name = "Fornecedor"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Bem (permanente e de consumo)
class Good(models.Model):
    name = models.CharField(max_length=100)
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
    identifier = models.CharField()
    phone_number = models.PositiveIntegerField()
    slug="claimant"
    localized_class_name = "Requerente"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Empréstimo
class Loan(models.Model):
    good = models.ForeignKey(Good, on_delete = models.PROTECT)
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT)
    loan_date = models.DateField()
    return_date = models.DateField()
    quantity = models.PositiveBigIntegerField()
    slug = "loan"
    localized_class_name = "Empréstimo"

    def __str__(self):
        return str(self.good.name) + " para " + str(self.claimant.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

    def due_check(self):
        return date.today() > self.return_date

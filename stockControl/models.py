from django.db import models
from django.urls import reverse
from datetime import date


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="nome")
    phone_number = models.CharField(max_length=20, verbose_name="telefone")
    slug = "supplier"

    class Meta:
        verbose_name = "Fornecedor"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Bem (permanente e de consumo)
class Good(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="nome")
    quantity = models.PositiveBigIntegerField(verbose_name="quantidade")
    acquisition_date = models.DateField(verbose_name="data de aquisição")
    description = models.TextField(verbose_name="descrição")
    status = models.CharField(max_length=30, verbose_name="status")
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name="fornecedor")
    permanent = models.BooleanField(verbose_name="permanente")
    warranty_expiry_date = models.DateField(verbose_name="data de vencimento da garantia")
    warranty_details = models.TextField(verbose_name="detalhes da garantia");
    slug = "good"

    class Meta:
        verbose_name = "Bem"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Requerente (Pessoa que empresta um bem)
class Claimant(models.Model):
    name = models.CharField(verbose_name="nome")
    identifier = models.CharField(unique=True, verbose_name="identificador")
    phone_number = models.CharField(max_length=20, verbose_name="telefone")
    slug="claimant"

    class Meta:
        verbose_name = "Requerente"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

# Empréstimo
class Loan(models.Model):
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT, verbose_name="requerente")
    loan_date = models.DateField(verbose_name="data do empréstimo")
    return_date = models.DateField(verbose_name="prazo de devolução")
    slug = "loan"

    class Meta:
        verbose_name = "Empréstimo"

    def __str__(self):
        return "Empréstimo " + str(self.id)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

    def due_check(self):
        return date.today() > self.return_date

# Item de empréstimo
class LoanItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.PROTECT, verbose_name="bem")
    loan = models.ForeignKey(Loan, on_delete=models.PROTECT, verbose_name="empréstimo")
    quantity = models.PositiveIntegerField(verbose_name="quantidade")
    slug = 'loan-item'

    class Meta:
        verbose_name = "Item de empréstimo"

    def __str__(self):
        return "Item de Empréstimo " + str(self.good.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

from datetime import date
from django.db import models
from django.urls import reverse
from datetime import date
from django.core.validators import MinValueValidator
from django.utils.ipv6 import ValidationError


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
    quantity = models.PositiveIntegerField(verbose_name="quantidade", validators=[MinValueValidator(1)])
    acquisition_date = models.DateField(verbose_name="data de aquisição")
    description = models.TextField(verbose_name="descrição")
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

    def get_loaned_quantity(self):
        return LoanItem.objects.filter(good=self, returned=False) \
                               .aggregate(total=models.Sum('quantity'))['total'] or 0

    def get_available_quantity(self):
        return self.quantity - self.get_loaned_quantity()

    def has_available_units(self):
        return self.get_loaned_quantity() < self.quantity

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

    def get_due_loans(self):
        return Loan.objects.filter(claimant=self, return_date__lt=date.today())

    def due_check(self):
        return self.get_due_loans().count() > 0

    def get_on_time_loans(self):
        return Loan.objects.filter(claimant=self, return_date__gte=date.today())

    def get_on_time_loan_count(self):
        return Loan.objects.filter(claimant=self, return_date__gte=date.today()).count()


# Empréstimo
class Loan(models.Model):
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT, verbose_name="requerente")
    loan_date = models.DateField(verbose_name="data do empréstimo")
    return_date = models.DateField(verbose_name="prazo de devolução")
    slug = "loan"

    class Meta:
        verbose_name = "Empréstimo"

    def __str__(self):
        loan = Loan.objects.get(pk=self.id)
        loan_items = LoanItem.objects.filter(loan=loan)
        if loan_items.count() < 1:
            return "Empréstimo " + str(self.id) + " (vazio)"
        elif loan_items.count() == 1:
            return "Empréstimo de " + str(loan_items[0])
        elif loan_items.count() == 2:
            return "Empréstimo de " + str(loan_items[0]) + " +" + str(loan_items.count() - 1) + " item"
        else:
            return "Empréstimo de " + str(loan_items[0]) + " +" + str(loan_items.count() - 1) + " itens"

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

    def due_check(self):
        return date.today() > self.return_date

    def returned_check(self):
        return LoanItem.objects.filter(loan=self).filter(returned=False).count() == 0

    def get_status(self):
        if self.returned_check():
            return "Devolvido"
        elif not self.returned_check() and self.due_check():
            return "Atrasado"
        else:
            return "Pendente"

# Item de empréstimo
class LoanItem(models.Model):
    good = models.ForeignKey(Good, on_delete=models.PROTECT, verbose_name="bem")
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, verbose_name="empréstimo")
    quantity = models.PositiveIntegerField(verbose_name="quantidade", validators=[MinValueValidator(1)])
    returned = models.BooleanField(verbose_name="devolvido", default=False)
    slug = 'loan-item'

    class Meta:
        verbose_name = "Item de empréstimo"

    def __str__(self):
        return str(self.good.name)

    def get_absolute_url(self):
        return reverse(self.slug + "-detail", kwargs={"pk": self.pk})

    def get_status(self):
        if self.returned:
            return "Devolvido"
        else:
            return "Emprestado"

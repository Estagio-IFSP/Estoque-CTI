from django.db import models


# Fornecedor
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    def get_slug(self):
        return "supplier"

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

    def __str__(self):
        return str(self.name)

    def get_slug(self):
        return "good"

# Requerente (Pessoa que empresta um bem)
class Claimant(models.Model):
    name = models.CharField()
    identifier = models.CharField()
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name) + " (" + str(self.identifier) + ")"

    def get_slug(self):
        return "claimant"

# Empréstimo
class Loan(models.Model):
    good = models.ForeignKey(Good, on_delete = models.PROTECT)
    claimant = models.ForeignKey(Claimant, on_delete = models.PROTECT)
    loan_date = models.DateField()
    return_date = models.DateField()
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.good.name) + " de " + str(self.loan_date) + " a " \
            + str(self.return_date) + " por " + str(self.claimant.name)

    def get_slug(self):
        return "loan"

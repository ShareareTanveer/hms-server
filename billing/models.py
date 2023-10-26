from decimal import Decimal
from django.db import models
from healthcare.models import Doctor
from patient.models import Patient


ACCOUNT_TYPE_CHOICES = (
    ('D', 'Debit'),
    ('C', 'Credit'),
)
PAYMENT_METHOD_CHOICES = (
    ('CASH', 'Cash'),
    ('CARD', 'Card'),
    ('CHEQUE', 'Cheque'),
)

#  ACCOUNTS
class Account(models.Model):
    account_name = models.CharField(max_length=5)
    account_type = models.CharField(max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.account_name


class Invoice(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    grand_total = models.DecimalField(
        max_digits=8, decimal_places=2, default=0)
    paid = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    due = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return Decimal(self.quantity) * self.price

    def save(self, *args, **kwargs):
        self.grand_total = self.subtotal() + (self.subtotal() * self.vat / 100) - \
            (self.subtotal() * self.discount / 100)
        self.due = self.grand_total - self.paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice #{self.pk} - {self.patient} - {self.date}"


class AccountPayment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.DateField()
    pay_to = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Payment #{self.pk} - {self.pay_to} - {self.date}"



# Billing 
class Service(models.Model):
    service_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Servive #{self.pk} - {self.service_name} - {self.rate}"


class Package(models.Model):
    package_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    discount = models.PositiveSmallIntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"Package #{self.pk} - {self.package_name} - {self.service}"


class PatientAdmission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField(null=True, blank=True)
    package_name = models.CharField(max_length=255, null=True, blank=True)
    insurance_name = models.CharField(max_length=255, null=True, blank=True)
    policy_no = models.CharField(max_length=50, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_name = models.CharField(max_length=255, null=True, blank=True)
    guardian_relation = models.CharField(max_length=50, null=True, blank=True)
    guardian_contact = models.CharField(max_length=20, null=True, blank=True)
    guardian_address = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.admission_date}"


class Bill(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    admission = models.ForeignKey(PatientAdmission, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_method = models.CharField(
        max_length=6, choices=PAYMENT_METHOD_CHOICES)
    date = models.DateField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vat_percent = models.DecimalField(max_digits=5, decimal_places=2)
    discount_percent = models.DecimalField(max_digits=5, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    due_amount = models.DecimalField(max_digits=8, decimal_places=2)
    receipt_no = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Bill #{self.pk} - {self.patient} - {self.date}"


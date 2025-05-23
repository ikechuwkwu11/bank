from django.db import models
from App.models import Customer, BankAccount
from django.utils import timezone

class Admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    is_customer = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BankStaff(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('manager','Manager'),('auditor','Auditor'),('teller','Teller')])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.name} ({self.role})'


class AccountApproval(models.Model):
    account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(BankStaff, on_delete=models.SET_NULL, null=True,blank=False)
    approved_on = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account.owner.username} - {'Approved' if self.is_approved else 'Pending'}"




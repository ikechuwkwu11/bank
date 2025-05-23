from django.db import models
from django.utils import timezone

class Customer(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password= models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(max_digits=30, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)


    def deposit(self,amount):
        self.balance += amount
        self.save()
        return self.balance

    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            self.save()
            return True
        return False


class BankAccount(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10, unique=True)
    type_of_card = models.CharField(max_length=20, choices=[('visa','Visa'),('master card','Master Card'),('verve','Verve')])
    created_at = models.DateTimeField(default=timezone.now)



class Transactions(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE)
    transaction_type = [('deposit', 'Deposit'), ('transfer', 'Transfer'), ('withdrawal', 'Withdrawal')]
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20,choices=transaction_type)
    date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.type.title()} of ${self.amount}"



class Transfer(models.Model):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='sent_transfers')
    recipient = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.sender.withdraw(self.amount):
            self.recipient.deposit(self.amount)
            super().save(*args, **kwargs)
        else:
            raise ValueError("Insufficient funds for transfer")

class BillPayment(models.Model):
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.customer.withdraw(self.amount):
            super().save(*args,**kwargs)
        else:
            raise ValueError("Insufficient funds for transfer")

class AirtimePurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    amount = models.DecimalField(max_digits=12,decimal_places=2)
    network = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.customer.withdraw(self.amount):
            super().save(*args, **kwargs)
        else:
            raise ValueError("Insufficient funds for airtime")


class BankStatement(models.Model):
    bank_account = models.ForeignKey(BankAccount, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Statement for {self.bank_account.account_number} from {self.start_date} to {self.end_date}"





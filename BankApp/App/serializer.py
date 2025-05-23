from rest_framework import serializers
from .models import Customer,BankAccount,BankStatement,BillPayment,AirtimePurchase,Transactions,Transfer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields = '__all__'

    def create(self, validated_data):
        # Optionally hash the password here
        customer = Customer.objects.create(**validated_data)
        return customer

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Customer
        fields = ['username', 'password']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    user = CustomerSerializer()
    class Meta:
        model = Transactions
        fields = '__all__'

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

class BillPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillPayment
        fields = '__all__'

class AirtimePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirtimePurchase
        fields = '__all__'

class BankStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankStatement
        fields = '__all__'


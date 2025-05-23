from rest_framework import serializers
from.models import Admin,BankStaff,AccountApproval


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = Admin
        fields = ['name','password']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class BankStaffSerializer(serializers.ModelSerializer):
    user = AdminSerializer()
    class Meta:
        model = BankStaff
        fields= '__all__'


class AccountApprovalSerializer(serializers.ModelSerializer):
    user = BankStaffSerializer()
    class Meta:
        model = AccountApproval
        fields = '__all__'
from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import RegisterSerializer,LoginSerializer,AdminSerializer,BankStaffSerializer,AccountApprovalSerializer
from django.contrib.auth import logout
from .models import Admin,BankStaff,AccountApproval
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from App.serializer import TransactionSerializer, CustomerSerializer
from App.models import Transactions,Customer

@method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered'},status=201)
            return Response(serializer.errors,status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response({'message':'You have successfully logged in','data':serializer.data},status=200)
            return Response({'message':'Please this did not work with your register, try again'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have logged out'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class PostAdmin(APIView):
    def put(self,request,admin_id):
        try:
            admin = Admin.object.get(id=admin_id)
            if not admin:
                return Response({'message':'Admin not found'},status=404)
            serializer = AdminSerializer(data=request.data )
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'the admin has been updated'},status=201)
            return Response(serializer.errors,status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)


class GetAdmin(APIView):
    def get(self,request):
        try:
            admin = Admin.objects.all()
            serializer = AdminSerializer(admin, many=True)
            return Response({'message':'This are all the admins','data':serializer.data},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class GetSingleAdmin(APIView):
    def get(self,request,admin_id):
        try:
            admin = Admin.objects.get(id=admin_id)
            serializer = AdminSerializer(admin)
            return Response({'message':'This is the profile of this particular admin','data':serializer.data},status=200)
        except Admin.DoesNotExist:
            return Response({'message':'This admin does not exist in this bank'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class AddBankStaff(APIView):
    def post(self,request):
        try:
            serializer = BankStaffSerializer(data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have been added to the bank portal'},status=201)
            return Response(serializer.errors,status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class GetBankStaff(APIView):
    def get(self,request):
        try:
            bankstaff = BankStaff.objects.all()
            serializer = BankStaffSerializer(bankstaff, many=True)
            return Response({'message':'This is the data of all bank staffs','data':serializer.data},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class GetSingleBankStaff(APIView):
    def get(self,request,bankstaff_id):
        try:
            bankstaff = BankStaff.objects.get(id=bankstaff_id)
            serializer = BankStaffSerializer(bankstaff)
            return Response({'message':'This is the data of a particular staff:','data':serializer.data},status=200)
        except BankStaff.DoesNotExist:
            return Response({'message':'This data does not exist'})
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class GetCustomer(APIView):
    def get(self,request):
        try:
            customer = Customer.objects.all()
            serializer = CustomerSerializer(customer, many=True)
            return Response({'message':'This are all the customers','data':serializer.data},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class GetSingleCustomer(APIView):
    def get(self,request,customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer)
            return Response({'message':'This is the customer details of this particular ID','data':serializer.data},status=200)
        except Customer.DoesNotExist:
            return Response({'message':'This customer does not exist here'},status=404)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class TransactionAll(APIView):
    def get(self,request):
        try:
            transaction = Transactions.objects.all()
            serializer = TransactionSerializer(transaction,many=True)
            return Response({'message':'this all are the transactions','data':serializer.data},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class TransactionSingle(APIView):
    def get(self,request,transactions_id):
        try:
            transaction = Transactions.objects.get(id=transactions_id)
            serializer = TransactionSerializer(transaction)
            return Response({'message':'This is the transaction for this particular user','data':serializer.data},status=200)
        except Transactions.DoesNotExist:
            return Response({'message':'This transaction does not exist'},status=400)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)




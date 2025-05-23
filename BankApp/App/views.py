from django.core.serializers import serialize
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer,BankAccount,Transactions,Transfer,BillPayment,AirtimePurchase,BankStatement
from .serializer import RegisterSerializer,LoginSerializer,CustomerSerializer,BankAccountSerializer,TransactionSerializer,TransferSerializer,BankStatementSerializer,BillPaymentSerializer,AirtimePurchaseSerializer
import random
from decimal import Decimal

class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                user= serializer.save()
                bank_account = BankAccount.objects.create(
                    user = user,
                    account_number = random.randint(1000000000, 9999999999),
                    type_of_card = 'master card'

                )
                bank_account.save()

                return Response({'message':'You have been registered. login now'},status=201)
            return Response(serializer.errors, status=404)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                return Response({'message':'you have logged in','data':serializer.data},status=200)
            return Response(serializer.errors,status=404)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class UpdateCustomer(APIView):
    def put(self,request,customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            if not customer:
                return Response({'message':'This customer does not have an account here!!'},status=404)

            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your profile has been updated'},status=200)
            return Response(serializer.errors, status=404)
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

class Deposit(APIView):
    def post(self,request,customer_id):
        try:
            amount = request.data.get("amount")
            if not amount:
                return Response({'message':'Amount must be required'},status=404)
            customer = Customer.objects.get(id=customer_id)
            if not customer:
                return Response({'message':'Customer does not exist'},status=404)
            customer.deposit(Decimal(amount))
            customer.save()
            transaction = Transactions.objects.create(
                user = customer,
                type = 'deposit',
                amount = amount
            )
            transaction.save()
            return Response({'message':f'Deposit of #{amount} was successful'},status=200)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=500)

class Withdraw(APIView):
    def post(self,request,customer_id):
        try:
            amount = request.data.get("amount")
            if not amount:
                return Response({'message': 'Amount must be required'}, status=404)
            customer = Customer.objects.get(id=customer_id)
            if not customer:
                return Response({'message': 'Customer does not exist'}, status=404)

            customer.withdraw(Decimal(amount))
            customer.save()
            transaction = Transactions.objects.create(
                user=customer,
                type='withdraw',
                amount=amount
            )
            transaction.save()
            return Response({'message': f'Withdrawal of #{amount} was successful'}, status=200)
        except Exception as e:
            return Response({'message': 'internal server error', 'error': str(e)}, status=500)

class Transfer(APIView):
    def post(self,request,customer_id):
        sender = request.objects.get(Customer, id=customer_id)

        data = request.data.copy()
        data['sender'] = sender.id  # Inject sender ID into serializer data

        # Validate recipient exists
        recipient_id = data.get('recipient')
        if not recipient_id:
            return Response({'message': 'Recipient ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            recipient = Customer.objects.get(id=recipient_id)
        except Customer.DoesNotExist:
            return Response({'message': 'Recipient does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TransferSerializer(data=data)

        if serializer.is_valid():
            amount = Decimal(serializer.validated_data['amount'])
            try:
                transfer = Transfer(
                    sender=sender,
                    recipient=recipient,
                    amount=amount
                )
                transfer.save()
                return Response(TransferSerializer(transfer).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BillPayment(APIView):
    def post(self,request,customer_id):
        try:
            customer = request.objects.get(Customer,id = customer_id)
            if not customer:
                return Response({'message':'This customer is not here'},status=404)

            data= request.data.copy()
            data['customer'] = customer_id

            serializer = BillPaymentSerializer(data=data)

            if serializer.is_valid():
                amount = Decimal(serializer.validated_data['amount'])
                bill_type = serializer.validated_data['bill_type']

                bill_payment = BillPayment(
                    customer=customer,
                    amount=amount,
                    bill_type=bill_type
                )
                bill_payment.save()
                return Response(BillPaymentSerializer(bill_payment).data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BankStatement(APIView):
    def get(self,request):
        try:
            bankstatement = request.objects.all()
            serializer = BankStatementSerializer(bankstatement)
            return Response({'message':'This is your bank statements','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
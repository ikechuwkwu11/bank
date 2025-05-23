from django.urls import path
from .views import Register,Login,Logout,PostAdmin,GetAdmin,GetSingleAdmin,AddBankStaff,GetBankStaff,GetSingleBankStaff,GetCustomer,GetSingleCustomer,TransactionAll,TransactionSingle

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('post-admin/',PostAdmin.as_view(),name='post-admin'),
    path('get-admin/',GetAdmin.as_view(),name='get-admin'),
    path('get-single-admin/<int:admin_id>',GetSingleAdmin.as_view(),name='get-single-admin'),
    path('add-bank-staff/',AddBankStaff.as_view(),name='add-bank-staff'),
    path('get-bank-staff/',GetBankStaff.as_view(),name='get-bank-staff'),
    path('get-single-bank-staff/<int:bankstaff_id>',GetSingleBankStaff.as_view(),name='get-single-bank-staff'),
    path('get-customer/',GetCustomer.as_view(),name='get-customer'),
    path('get-single-customer/<int:customer_id>',GetSingleCustomer.as_view(),name='get-single-customer'),
    path('transaction-all/',TransactionAll.as_view(),name='transaction-all'),
    path('transaction-single/<int:transactions_id>',TransactionSingle.as_view(),name='transaction-single')

]
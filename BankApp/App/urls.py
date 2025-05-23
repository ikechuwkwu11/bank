from django.urls import path
from .views import Register,Login,UpdateCustomer,GetSingleCustomer,Deposit,Withdraw,Transfer

urlpatterns = [
    path('register',Register.as_view(),name='register'),
    path('login',Login.as_view(),name='login'),
    path('update-customer/<int:customer_id>',UpdateCustomer.as_view(),name='update-customer'),
    path('get-single-customer/<int:customer_id>',GetSingleCustomer.as_view(),name='get-single-customer'),
    path('deposit/<int:customer_id>',Deposit.as_view(),name='deposit'),
    path('withdraw/<int:customer_id>',Withdraw.as_view(),name='withdraw'),
    path('transfer/<int:customer_id>',Transfer.as_view(),name = 'transfer')
]
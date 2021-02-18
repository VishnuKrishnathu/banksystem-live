from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('customers', views.customers, name = 'customers'),
    path('customers/<str:first_name>', views.customer_data, name = 'customer'),
    path('customers/<str:first_name>/paymentdone', views.paymentdone , name = 'paymentdone'),
]
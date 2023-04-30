from django.urls import path
from .views import desktop,contact,price,service

urlpatterns = [
    
    path('', desktop, name='desktop' ),
    path('contact', contact, name='contact' ),
    path('price', price, name='price' ),
    path('service', service, name='service' ),
]

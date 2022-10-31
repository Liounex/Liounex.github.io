from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home , name='inicio'),
    path('Nosotros/', views.About, name='nosotros'),
    path('Productos/', views.Product, name='productos'),
    path('Contacto/', views.Contact.as_view(), name='contacto')
    #path('Contacto/', views.Contact, name='contacto'),
]
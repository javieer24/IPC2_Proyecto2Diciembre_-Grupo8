from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home/', views.Inicio, name='Inicio'),
    path('document/', views.Documentation, name='Documentacion'),
    path('clientes/', views.Clientes, name='Clientes'),
    path('productos/', views.Productos_List, name='Productos'),
    path('factura/', views.Factura, name='Factura'),

 
    
]

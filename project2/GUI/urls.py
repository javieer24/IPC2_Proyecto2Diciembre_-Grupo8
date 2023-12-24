from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('home/', views.Inicio, name='Inicio'),
    path('document/', views.Documentation, name='Documentacion'),
]

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import os
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import requests
from .models import first_products as Productos, xml_replace as xml
from Backend.method.product import Producto
from Backend.method.clients import Cliente



# Create your views here.
def Home(request):
    return render(request, 'publicacion/index.html', {})

def Inicio(request):
    return render(request, 'publicacion/inicio.html', {})

def Clientes(request):
    return render(request, 'publicacion/clientes.html', {})

def Productos_List(request):
    return render(request, 'publicacion/productos.html', {})

def Factura(request):
    return render(request, 'publicacion/factura.html', {})

def Documentation(request):
    context = {
        'STATIC_URL': '/static/',
    }
    return render (request, 'publicacion/document.html', context)


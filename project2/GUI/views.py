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

def Documentation(request):
    context = {
        'STATIC_URL': '/static/',
    }
    return render (request, 'publicacion/document.html', context)

def index(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        for producto in Productos:
            if producto.id == id:
                producto.downStock()
                producto.aniadir_lista(Productos)
                break
        return render(request, 'publicacion/public.html',{
            "productos": Productos
        })
    else:
        if not request.GET.get('search'):
            return render(request, 'publicacion/public.html',{
                "productos": Productos
            })
        else:
            busqueda = request.GET.get('publicacion/public.html')
            productos = []
            for producto in Productos:
                if busqueda.lower() in producto.nombre.lower():
                    productos.append(producto)
            return render(request, 'publicacion/public.html',{
                "productos": productos
            })
            
def edit(request, id=None):
    if request.method == 'GET':
        id = int(request.POST.get('id'))
        for producto in Productos:
            if producto.id == id:
                producto.downStock()
                producto.aniadir_lista(Productos)
                break
        return render(request, 'home.html',{
            "productos": Productos
        })
    else:
        if not request.GET.get('busqueda'):
            return render(request, 'publicacion/public.html',{
                "productos": Productos
            })
        else:
            busqueda = request.GET.get('busqueda')
            productos = []
            for producto in Productos:
                if busqueda.lower() in producto.nombre.lower():
                    productos.append(producto)
            return render(request, 'publicacion/public.html',{
                "productos": productos
            })
         
def new(request):
    if request.method == 'GET':
        return render(request, 'crear.html')
    else:
        try:
            id = Productos[-1].id + 1
            nombre = request.POST.get('nombre')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            stock = int(request.POST.get('stock'))
            new_product = Producto(id, nombre, descripcion, precio, stock)
            Productos.append(new_product)
            xml()
            return redirect('/')
        except:
            return redirect('/Crear_Producto/', {
                'error': 'Coloque valores válidos'
            })
            
            
def eliminar(request):
    if request.method == 'POST':
        id = int(request.POST.get('id'))
        for producto in Productos:
            if producto.id == id:
                Productos.remove(producto)
                break
        xml()    
        return redirect('/')

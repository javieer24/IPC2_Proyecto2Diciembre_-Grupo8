from django.db import models

# Create your models here.
class Clientes(models.Model):
    codigo = models.CharField(max_length = 300, null = True, blank = True)
    nombre = models.CharField(max_length=300)
    apellido = models.CharField(max_length=300)
    email = models.EmailField()
    telefono = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
    created = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField( auto_now_add=True)
    
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    codigo = models.CharField(max_length = 200, null = True, blank = True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=100)
    stock = models.CharField(max_length=100)
    created = models.DateTimeField( auto_now_add=True)
    update = models.DateTimeField( auto_now_add=True)
    
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['nombre']
    
    
    def __str__(self):
        return self.nombre
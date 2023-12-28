# **Manual Técnico**

Requisitos minimos del Sistema Operativo para ejecutar el programa:

- Windows 10 (8u51 y superiores)
- Windows 8.x (escritorio)
- Windows 7 SP1
- Windows Vista SP2
- RAM: 128MB
- Espacio en Disco: 124 MB para python
- Procesador: Minimo Pentium 2 a 266 M

## ⚒ Requerimientos
<ul>
    <li>Python 3.11.5 o Superior</li>
    <li>Matplotlib</li>
    <li>Reportlab</li>

</ul>

## 🗂 Recursos
<ul>
  <li><a href="https://www.python.org/downloads/release/python-3115/">Python 3.11.5 o Superior</a></li>
  <li><a href="https://www.reportlab.com/">Matplotlib</a></li>
  <li><a href="https://matplotlib.org/">ReportLab</a></li>
</ul>

También puede instalarlo usando pip
Para matplotlib

```js
pip install matplotlib
```
Para reportlab

```js
pip install reportlab
```

## **Descripción General**
El presente proyecto consiste en el desarrollo de un reproductor de música que utiliza un archivo XML para almacenar la información sobre las canciones. El reproductor debe ser capaz de leer el archivo XML, mostrar una lista de las canciones, reproducir las canciones y mostrar la imagen de la canción que se está reproduciendo junto con su archivo mp3.

# Estructura Proyecto 1, carpetas  y archivos
~~~
IPC2_Proyecto1Diciembre_-Grupo8
├── Documentación
│   └── Manual Tecnico
│   │   ├── README.md
│   ├── Manual de Usuario
│   │   ├── IMG
|   |   |   ├──imagenes png para el readme.md
│   │   ├── README.md
│   └── Documentación
│   └── Proyecto 2 - IPC2.pdf
├── IMG
│   └── imagenes png para el readme.md inicial
├── project2
│   ├── Backend
│   │   ├──method
|   │   │   ├──__pycache__
|   |   |   |──__init__.py
|   |   |   |──clients.py
|   |   |   |──factura.py
|   |   |   |──product.py
|   |   |   |──readxml.py
│   │   ├──main.py
│   ├── GUI
│   │   ├──__pycache__
│   │   ├──migrations
|   |   |   |__pycache__
|   |   |   |__init__.py
│   │   ├──static
|   |   |   |──Documentacion.pdf
|   |   |   |──estilos.css
|   |   |   |──logo.png
|   |   |   |──logo3.png
|   |   |   |──plantilla.css
│   │   ├──templates
|   |   |   |──publicacion
|   |   |   |   |──clientes.html
|   |   |   |   |──document.html
|   |   |   |   |──factura.html
|   |   |   |   |──index.html
|   |   |   |   |──inicio.html
|   |   |   |   |──productos.html
│   │   ├──__init__.py
│   │   ├──admin.py
│   │   ├──apps.py
│   │   ├──cliente.xml
│   │   ├──factura.xml
│   │   ├──forms.py
│   │   ├──models.py
│   │   ├──stock.xml
│   │   ├──tests.py
│   │   ├──urls.py
│   │   ├──views.py
│   ├── project2
│   │   ├──__pycache__
│   │   ├──__init__.py
│   │   ├──asgi.py
│   │   ├──settings.py
│   │   ├──urls.py
│   │   ├──wsgi.py
│   ├── db.sqlite3
|   ├── manage.py
├── .gitignore
├── README.md
~~~

## **Paradigma de Programación**
Todo el desarrollo del programa está basado en el paradigma de programación orientado a objetos, esto es, un modelo o un estilo de programación que proporciona unas guías acerca de cómo trabajar con él y que está basado en el concepto de clases y objetos.

Es por ello que durante toda la realización del programa se implementó el uso de clases, clases abstractas y objetos de las mismas.


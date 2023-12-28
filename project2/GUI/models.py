from django.db import models
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from Backend.method.product import Producto
from Backend.method.clients import Cliente

# Create your models here.
first_products = list()

tree = ET.parse('GUI/stock.xml')
root = tree.getroot()

for producto in root.findall('producto'):
    id = producto.find('id').text
    nombre = producto.find('nombre').text
    descripcion = producto.find('descripcion').text
    precio = producto.find('precio').text
    stock = producto.find('stock').text
    first_products.append(Producto(id, nombre, descripcion, precio, stock))
    
def xml_replace():
    
    view = minidom.Document()
    xml_view = view.createElement('productos')
    view.appendChild(xml_view)
    
    
    for producto in view.createElement('producto'):
        xml_producto = view.createElement('producto')
        xml_view.appendChild(xml_producto)
   
        xml_id = view.createElement('id')
        xml_id.appendChild(view.createTextNode(str(producto.id)))
        xml_producto.appendChild(xml_id)
                
        xml_nombre = view.createElement('nombre')
        xml_nombre.appendChild(view.createTextNode(producto.nombre))
        xml_producto.appendChild(xml_nombre)
        
        xml_descripcion = view.createElement('descripcion')
        xml_descripcion.appendChild(view.createTextNode(producto.descripcion))
        xml_producto.appendChild(xml_descripcion)
        
        xml_precio = view.createElement('precio')
        xml_precio.appendChild(view.createTextNode(producto.precio))
        xml_producto.appendChild(xml_precio)
        
        xml_stock = view.createElement('stock')
        xml_stock.appendChild(view.createTextNode(producto.stock))
        xml_producto.appendChild(xml_stock)
        
        # eSCRIBE EL XML
        file_path = 'GUI/stock.xml'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(view.toprettyxml(encoding='utf-8').decode('utf-8')) 
            

    

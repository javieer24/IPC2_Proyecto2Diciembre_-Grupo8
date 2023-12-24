import xml.etree.ElementTree as ET
import os


class ReadXML:
    def __init__(self, xml_file):
        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def read_stock(self):
        for producto in self.root.findall('producto'):
            nombre = producto.find('nombre').text
            descripcion = producto.find('descripcion').text
            precio = producto.find('precio').text
            stock = producto.find('stock').text
            print(f'Nombre: {nombre}, Descripción: {descripcion}, Precio: {precio}, Stock: {stock}')

    def read_cliente(self):
        for cliente in self.root.findall('cliente'):
            nit = cliente.find('nit').text
            nombre = cliente.find('nombre').text
            direccion = cliente.find('direccion').text
            print(f'Nit: {nit}, Nombre: {nombre}, Dirección: {direccion}')

    def read_factura(self):
        for factura in self.root.findall('factura'):
            maestro = factura.find('maestro').text
            detalle = factura.find('detalle').text
            print(f'Maestro: {maestro}, Detalle: {detalle}')

# Uso de la clase
stock = ReadXML('stock.xml')
stock.read_stock()

cliente = ReadXML('cliente.xml')
cliente.read_cliente()

factura = ReadXML('factura.xml')
factura.read_factura()

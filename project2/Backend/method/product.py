class Producto():
    def __init__(self, id, nombre, descripcion, precio, stock ):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.lista = list()
        
    def add_lista(self, list):
        self.lista = list
        
    def deleteProducto(self):
        self.lista.remove(self)
        
    def downStock(self):
        if self.stock > 1:
            self.stock -= 1
        else:
            self.eliminarProducto() 
        return self.stock
    
    mas_vendidos_ids = [2, 4, 1]

    def es_mas_vendido(self):
        return self.id in Producto.mas_vendidos_ids

    def ranking_ventas(self):
        if self.es_mas_vendido():
            return Producto.mas_vendidos_ids.index(int(self.id)) + 1
        return float('inf')
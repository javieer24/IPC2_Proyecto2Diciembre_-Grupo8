# Clase para Cliente
class Cliente():
    def __init__(self, id, nit, nombre, mail, phone, direccion):
        self.id = id
        self.nit = nit
        self.nombre = nombre
        self.mail = mail
        self.phone = phone
        self.direccion = direccion
        self.list_clients = list()
        
    
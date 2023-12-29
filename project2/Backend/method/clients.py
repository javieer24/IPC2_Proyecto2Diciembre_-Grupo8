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
        
    #clientes_prioritarios_ids = [3, 5, 1]

    #def es_cliente_prioritario(self):
    #    return self.id in Cliente.clientes_prioritarios_ids

    #def ranking_clientes(self):
    #    if self.es_cliente_prioritario():
    #        return Cliente.clientes_prioritarios_ids.index(self.id) + 1
    #    return float('inf')
    
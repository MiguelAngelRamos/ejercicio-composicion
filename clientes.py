from prettytable import PrettyTable

class Cliente:
    def __init__(self, id, nombre, email, saldo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.saldo = saldo

list_clientes = [
    Cliente("C001", "Laura Martínez", "laura.martinez@correo.com", 1500),
    Cliente("C002", "Sofia Navarro", "sofia.navarro@correo.com", 2000),
    Cliente("C003", "Carlos López", "carlos.lopez@correo.com", 1800),
    Cliente("C004", "Margarita Marquez", "margarita.marquez@correo.com", 2200),
    Cliente("C005", "Richard Stallman", "richard.stallman@correo.com", 3000),
]

def imprimir_clientes():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Email", "Saldo"]
    for cliente in list_clientes:
        tabla.add_row([cliente.id, cliente.nombre, cliente.email, cliente.saldo])
    print(tabla)
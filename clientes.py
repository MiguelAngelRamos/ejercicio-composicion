from prettytable import PrettyTable
from utils import input_con_opcion_de_salida
class Cliente:
    def __init__(self, id, nombre, email, saldo):
        self.id = id
        self.nombre = nombre
        self.email = email #TODO: Crear expresión regular para validación
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

# Agregar un cliente
def agregar_cliente():
    imprimir_clientes()
    print("\nAgregar nuevo cliente (escribe 'salir' para cancelar):")
    id = input_con_opcion_de_salida("ID: ")
    if id is None: return
    nombre = input_con_opcion_de_salida("Nombre: ")
    if nombre is None: return
    email = input_con_opcion_de_salida("Email: ")
    if email is None: return
    saldo = input_con_opcion_de_salida("Saldo: ")
    if saldo is None: return

    try:
        nuevo_cliente = Cliente(id, nombre, email, float(saldo))
        list_clientes.append(nuevo_cliente)
        print("Cliente agregado exitosamente.\n")
    except ValueError as error:
        print(f"Error al agregar el cliente: {error}")
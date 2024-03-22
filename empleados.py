from prettytable import PrettyTable
from utils import input_con_opcion_de_salida


class Empleado:
    def __init__(self, id, nombre, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario


list_empleados = [
    Empleado("E001", "Empleado Uno", "Gerente", 5000),
    Empleado("E002", "Empleado Dos", "Vendedor", 3000),
    Empleado("E003", "Empleado Tres", "Vendedor", 3000),
    Empleado("E004", "Empleado Cuatro", "Gerente", 5000),
    Empleado("E005", "Empleado Cinco", "Vendedor", 3000)
]


def imprimir_empleados():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Puesto", "Salario"]
    for empleado in list_empleados:
        tabla.add_row([empleado.id, empleado.nombre, empleado.puesto, empleado.salario])
    print(tabla)


## shift + alt + fecha hacia abajo

def agregar_empleado():
    imprimir_empleados()
    print("\n Agregar nuevo empleado (escribe 'salir' para cancelar):")

    id_empleado = input_con_opcion_de_salida("ID: ")
    if id_empleado is None: return

    nombre = input_con_opcion_de_salida("Nombre: ")
    if nombre is None: return

    puesto = input_con_opcion_de_salida("Puesto: ")
    if puesto is None: return

    salario = input_con_opcion_de_salida("Salario: ")
    if salario is None: return

    try:
        nuevo_empleado = Empleado(id_empleado, nombre, puesto, salario)
        list_empleados.append(nuevo_empleado)
        print("Empleado agregado exitosamente. \n")
    except ValueError as error:
        print(f"Error al agregar el empleado:{error}")

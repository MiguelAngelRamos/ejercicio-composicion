from prettytable import PrettyTable

class Empleado:
    def __init__(self, id, nombre, puesto, salario):
        self.id = id
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

empleados = [
    Empleado("E001", "Empleado Uno", "Gerente", 5000),
    Empleado("E002", "Empleado Dos", "Vendedor", 3000),
    Empleado("E003", "Empleado Tres", "Vendedor", 3000),
    Empleado("E004", "Empleado Cuatro", "Gerente", 5000),
    Empleado("E005", "Empleado Cinco", "Vendedor", 3000)
]

def imprimir_empleados():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Puesto", "Salario"]
    for empleado in empleados:
        tabla.add_row([empleado.id, empleado.nombre, empleado.puesto, empleado.salario])
    print(tabla)

imprimir_empleados()
## shift + alt + fecha hacia abajo

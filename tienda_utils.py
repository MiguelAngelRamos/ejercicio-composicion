from productos import list_productos, imprimir_productos
from clientes import list_clientes, imprimir_clientes
from empleados import list_empleados, imprimir_empleados

def input_con_opcion_de_salida(prompt):
    respuesta = input(prompt)
    # Salir salir SAliR
    if respuesta.lower() == "salir":
        print("Operación cancelada.")
        return None
    return respuesta


def encontrar_por_id(lista, id):
    for element in lista:
        if element.id == id:
            return element
    return None

def resumen_productos():
    if list_productos:
        print("Resumen de productos existentes")
        imprimir_productos()
    else:
        print("No hay productos registrados")

def resumen_clientes():
    if list_clientes:
        print("Resumen de clientes existentes")
        imprimir_clientes()
    else:
        print("No hay clientes registrados")
        
def resumen_empleados():
    if list_empleados:
        print("Resumen de empleados existentes")
        imprimir_empleados()
    else:
        print("No hay empleados registrados")


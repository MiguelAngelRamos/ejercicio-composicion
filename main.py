from productos import ProductoElectronico, imprimir_productos
from empleados import Empleado, imprimir_empleados
from clientes import Cliente, list_clientes, imprimir_clientes


def input_con_opcion_de_salida(prompt):
    respuesta = input(prompt)
    # Salir salir SAliR
    if respuesta.lower() == "salir":
        print("Operación cancelada.")
        return None
    return respuesta

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


def main():
    while True:
        print("""
Menú Principal:
              
    1. Agregar Productos Electrónico
    2. Agregar Cliente
    3. Agregar Empleado
    4. Realizar la venta
    5. Imprimir lista de Productos
    6. Imprimir lista de Clientes
    7. Imprimir lista de Empleados
    8. Imprimir ventas realizadas
    9. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            pass
        elif opcion == '2':
            agregar_cliente()
        elif opcion == '3':
            pass
        elif opcion == '4':
            pass
        elif opcion == '5':
            imprimir_productos()
        elif opcion == '6':
            imprimir_clientes()
        elif opcion == '7':
            imprimir_empleados()
        elif opcion == '8':
            pass
        elif opcion == '9':
            print("Saliendo del sistema....")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")



if __name__ == "__main__":
    main()
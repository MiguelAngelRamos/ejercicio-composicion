from productos import ProductoElectronico, imprimir_productos
from empleados import Empleado, imprimir_empleados
from clientes import Cliente, imprimir_clientes, agregar_cliente
from venta import ejecutar_venta
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
            ejecutar_venta()
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
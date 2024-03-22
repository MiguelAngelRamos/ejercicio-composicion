from tienda_utils import resumen_clientes, resumen_empleados, resumen_productos
from clientes import agregar_cliente
from venta import ejecutar_venta, imprimir_ventas
from empleados import agregar_empleado
from productos import agregar_producto


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
            agregar_producto()
        elif opcion == '2':
            agregar_cliente()
        elif opcion == '3':
            agregar_empleado()
        elif opcion == '4':
            ejecutar_venta()
        elif opcion == '5':
            resumen_productos()
        elif opcion == '6':
            resumen_clientes()
        elif opcion == '7':
            resumen_empleados()
        elif opcion == '8':
            imprimir_ventas()
        elif opcion == '9':
            print("Saliendo del sistema....")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()

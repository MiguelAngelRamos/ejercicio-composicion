from prettytable import PrettyTable
from datetime import datetime
from productos import list_productos
from clientes import list_clientes
from empleados import list_empleados
from tienda_utils import encontrar_por_id as encontrar_producto_por_id
from tienda_utils import encontrar_por_id as encontrar_cliente_por_id
from tienda_utils import encontrar_por_id as encontrar_empleado_por_id
from tienda_utils import resumen_productos, resumen_clientes, resumen_empleados
from utils import input_con_opcion_de_salida


class Venta:
    def __init__(self, id_venta, producto, cliente, empleado, fecha, cantidad):
        self.id_venta = id_venta
        self.producto = producto
        self.cliente = cliente
        self.empleado = empleado
        self.fecha = fecha
        self.cantidad = cantidad


list_ventas = []


def realizar_venta(id_venta, id_producto, id_cliente, id_empleado, cantidad):
    producto = encontrar_producto_por_id(list_productos, id_producto)
    cliente = encontrar_cliente_por_id(list_clientes, id_cliente)
    empleado = encontrar_empleado_por_id(list_empleados, id_empleado)

    if producto and cliente and empleado:
        if producto.stock >= cantidad and cliente.saldo >= producto.precio * cantidad:
            # producto.stock = producto.stock - cantidad
            producto.stock -= cantidad
            cliente.saldo -= producto.precio * cantidad
            venta = Venta(id_venta, producto, cliente, empleado, datetime.now(), cantidad)
            list_ventas.append(venta)
            # TODO: considerar impuestos
            print(f"Venta realizada exitosamente. ID de Venta: {id_venta}, Cantidad: {cantidad}")
        else:
            if producto.stock < cantidad:
                print("No hay suficiente stock del producto")
            if cliente.saldo < producto.precio * cantidad:
                print("El cliente no tiene saldo suficiente.")
    else:
        if not producto:
            print("Producto no encontrado.")
        if not cliente:
            print("Cliente no encontrado.")
        if not empleado:
            print("Empleado no encontrado.")


def imprimir_ventas():
    tabla = PrettyTable()
    tabla.field_names = ["ID Venta", "Producto", "Cliente", "Empleado", "Fecha", "Cantidad"]
    for venta in list_ventas:
        tabla.add_row([
            venta.id_venta,
            venta.producto.nombre,
            venta.cliente.nombre,
            venta.empleado.nombre,
            venta.fecha.strftime("%Y-%m-%d %H:%M"),
            venta.cantidad
        ])

    if len(list_ventas) == 0:
        print("No se han generado ventas")
    else:
        print(tabla)


def ejecutar_venta():
    print("\n Preparándose para realizar la venta...")
    # imprimir los productos, clientes y empleados "disponibles"
    resumen_productos()
    resumen_clientes()
    resumen_empleados()

    id_venta = input_con_opcion_de_salida("ID de Venta: ")
    if id_venta is None:
        return

    id_producto = input_con_opcion_de_salida("ID de producto: ")
    if id_producto is None:
        return

    id_cliente = input_con_opcion_de_salida("ID de cliente: ")
    if id_cliente is None:
        return

    id_empleado = input_con_opcion_de_salida("ID de empleado: ")
    if id_empleado is None:
        return

    cantidad = input_con_opcion_de_salida("ID de Cantidad: ")
    if cantidad is None:
        return

    try:
        cantidad = int(cantidad)
        realizar_venta(id_venta, id_producto, id_cliente, id_empleado, cantidad)
    except ValueError:
        print("Cantidad debe ser un numero entero")
    except Exception as Error:
        print(f"Error al realizar la venta {Error}")

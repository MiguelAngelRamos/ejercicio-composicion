from prettytable import PrettyTable
from utils import input_con_opcion_de_salida


class ProductoElectronico:
    def __init__(self, id, nombre, precio, categoria, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock


list_productos = [
    ProductoElectronico("P001", "Laptop Gamer", 1200, "Computadoras", 10),
    ProductoElectronico("P002", "Smartphone XYZ", 700, "Teléfonos", 15),
    ProductoElectronico("P003", "Auriculares Bluetooth", 150, "Accesorios", 20),
    ProductoElectronico("P004", "Monitor 4K", 400, "Monitores", 5),
    ProductoElectronico("P005", "Tablet Alfa", 300, "Tablets", 8),
    ProductoElectronico("P006", "Teclado Mecánico", 100, "Accesorios", 25),
    ProductoElectronico("P007", "Mouse Ergonómico", 50, "Accesorios", 30),
    ProductoElectronico("P008", "Cámara Web HD", 90, "Accesorios", 15),
    ProductoElectronico("P009", "Altavoces 2.1", 200, "Accesorios", 10),
    ProductoElectronico("P010", "Smartwatch", 250, "Wearables", 12)
]


def imprimir_productos():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Precio", "Categoria", "Stock"]
    for producto in list_productos:
        tabla.add_row([producto.id, producto.nombre, producto.precio, producto.categoria, producto.stock])
    print(tabla)


def agregar_producto():
    imprimir_productos()
    print("\n Agregar nuevo producto (escribe 'salir' para cancelar):")

    id_producto = input_con_opcion_de_salida("ID: ")
    if id_producto is None: return

    nombre = input_con_opcion_de_salida("Nombre: ")
    if nombre is None: return

    precio = input_con_opcion_de_salida("Precio: ")
    if precio is None: return

    categoria = input_con_opcion_de_salida("Categoria: ")
    if categoria is None: return

    stock = input_con_opcion_de_salida("Stock: ")
    if stock is None: return

    try:
        nuevo_producto = ProductoElectronico(id_producto, nombre, precio, categoria, stock)
        list_productos.append(nuevo_producto)
        print("Producto agregado exitosamente. \n")
    except ValueError as error:
        print(f"Error al agregar el producto:{error}")

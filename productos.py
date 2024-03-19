from prettytable import PrettyTable

class ProductoElectronico:
    def __init__(self, id, nombre, precio, categoria, stock):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        
productos = [
    ProductoElectronico("001", "Laptop Gamer", 1200, "Computadoras", 10),
    ProductoElectronico("002", "Smartphone XYZ", 700, "Teléfonos", 15),
    ProductoElectronico("003", "Auriculares Bluetooth", 150, "Accesorios", 20),
    ProductoElectronico("004", "Monitor 4K", 400, "Monitores", 5),
    ProductoElectronico("005", "Tablet Alfa", 300, "Tablets", 8),
    ProductoElectronico("006", "Teclado Mecánico", 100, "Accesorios", 25),
    ProductoElectronico("007", "Mouse Ergonómico", 50, "Accesorios", 30),
    ProductoElectronico("008", "Cámara Web HD", 90, "Accesorios", 15),
    ProductoElectronico("009", "Altavoces 2.1", 200, "Accesorios", 10),
    ProductoElectronico("010", "Smartwatch", 250, "Wearables", 12)
]
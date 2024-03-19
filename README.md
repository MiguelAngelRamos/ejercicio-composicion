### Enunciado del Ejercicio: Sistema de Gestión de Ventas con Composición en Python

#### Objetivo:
Desarrollar un sistema de gestión de ventas en Python que modele las interacciones entre productos, clientes, empleados y ventas, utilizando principios de la programación orientada a objetos, con especial énfasis en la composición para modelar relaciones entre objetos.

#### Requisitos:

1. **Gestión de Productos:**
   - Crea una clase `ProductoElectronico` con atributos para ID, nombre, precio, categoría y stock.
   - Implementa una función para agregar nuevos productos al sistema y otra para imprimir un resumen de todos los productos disponibles.

2. **Gestión de Clientes:**
   - Diseña una clase `Cliente` que contenga atributos para ID, nombre, email y saldo.
   - Desarrolla funciones para registrar nuevos clientes y mostrar un resumen de los clientes registrados.

3. **Gestión de Empleados:**
   - Define una clase `Empleado` con atributos para ID, nombre, puesto y salario.
   - Añade funciones para agregar empleados al sistema y listar todos los empleados existentes.

4. **Realización de Ventas con Composición:**
   - Implementa una clase `Venta` que incluya: ID de venta, producto vendido, cliente, empleado que realizó la venta, fecha y cantidad de productos vendidos.
   - **Aplica la composición** al incluir en cada `Venta` referencias directas a instancias específicas de `ProductoElectronico`, `Cliente` y `Empleado`, mostrando cómo estos componentes se relacionan en una transacción de venta.
   - Asegura que el sistema pueda procesar ventas, actualizando el stock del producto y el saldo del cliente correspondiente, y mantén un registro de cada venta en una lista de ventas realizadas.

5. **Menú Principal:**
   - Construye un menú interactivo en la consola que ofrezca opciones para agregar productos, clientes, empleados, realizar ventas, imprimir listas de productos, clientes, empleados y ventas realizadas, y la opción de salir del sistema.

6. **Funcionalidades Adicionales y Validaciones:**
   - Incorpora validaciones para garantizar que el stock del producto sea suficiente y que el cliente tenga saldo disponible antes de completar una venta.
   - Implementa una opción para "salir" en cada menú interactivo, permitiendo al usuario cancelar la acción en curso.

#### Aspectos Clave a Demostrar:
- **Composición:** Este proyecto debe evidenciar el uso efectivo de la composición para establecer relaciones significativas entre diferentes objetos (productos, clientes, empleados) dentro de una instancia de `Venta`.
- **Interacción con el Usuario:** Desarrolla una interfaz de usuario en consola clara y amigable que facilite la navegación por las diferentes opciones del sistema.


#### Crear el entorno Virtual

```sh
python -m venv tienda
```
#### Activar entorno virtual 

```sh
 tienda\Scripts\activate
```
#### Instalaciones necesarias
   ```sh
   pip install prettytable
   ```
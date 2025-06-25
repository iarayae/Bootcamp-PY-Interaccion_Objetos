# Bootcamp-PY-Interaccion_Objetos
Bootcamp - Python - Interacción entre objetos

El objetivo es diseñar un sistema de tiendas y productos con comportamiento distinto según el tipo de tienda, utilizando conceptos como encapsulamiento, herencia, composición y colaboración entre clases.

## Archivos del proyecto ##

- producto.py: contiene la clase `Producto`, con atributos encapsulados y métodos para consultar, modificar y operar sobre productos.
- tienda.py: contiene la clase base `Tienda` y las subclases `Restaurante`, `Supermercado` y `Farmacia`, cada una con lógica específica para agregar productos, listar productos y procesar ventas.
- programa.py: script principal que permite al usuario crear una tienda, ingresar productos, listar los productos existentes, realizar ventas o salir del programa.

## Funcionalidades principales ##

1. Crear una tienda
   - Se solicita al usuario el tipo de tienda, nombre y costo de delivery.
   - Tipos de tienda disponibles: Restaurante, Supermercado, Farmacia.

2. Ingresar productos
   - El usuario puede ingresar productos con nombre, precio y stock.
   - En Restaurantes, el stock siempre es 0 (los productos se preparan bajo demanda).

3. Listar productos
   - Supermercado muestra el stock y una advertencia si es menor a 10.
   - Farmacia no muestra el stock, pero indica si el producto tiene envío gratis (si cuesta más de $15.000).
   - Restaurante solo muestra nombre y precio.

4. Realizar ventas
   - Supermercado y Farmacia solo pueden vender si hay stock disponible.
   - Farmacia no permite vender más de 3 unidades por producto.
   - Si se solicita más de lo disponible, se vende solo lo que hay.
   - Restaurante no controla stock (siempre se puede vender).

5. Salir del sistema
   - El usuario puede cerrar el programa en cualquier momento seleccionando la opción correspondiente.
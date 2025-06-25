from tienda import Restaurante, Supermercado, Farmacia

# Solicitar datos para crear una tienda
print("Bienvenido al sistema de gestión de Tiendas.")
tipo = input("Ingrese el tipo de tienda (Restaurante / Supermercado / Farmacia): ").lower()
nombre = input("Ingrese el nombre de la tienda: ")
delivery = float(input("Ingrese el costo de delivery: "))

# Crear instancia de tienda según tipo ingresado
if tipo == "restaurante":
    tienda = Restaurante(nombre, delivery)
elif tipo == "supermercado":
    tienda = Supermercado(nombre, delivery)
elif tipo == "farmacia":
    tienda = Farmacia(nombre, delivery)
else:
    print("Tipo de tienda no válido.")
    exit()

# Agregar productos
while True:
    agregar = input("¿Desea agregar un producto? (s/n): ").lower()
    if agregar != "s":
        break
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Stock del producto (opcional, enter para 0): ") or 0)
    tienda.ingresar_producto(nombre, precio, stock)

# Menú principal de acciones
while True:
    print("\n¿Qué desea hacer?")
    print("1. Listar productos")
    print("2. Realizar venta")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Llamar a método listar
        print(tienda.listar_productos())
    elif opcion == "2":
        # Solicitar datos de venta
        nombre = input("Nombre del producto a vender: ")
        cantidad = int(input("Cantidad a vender: "))
        tienda.vender(nombre, cantidad)
        print("Venta procesada.")
    elif opcion == "3":
        # Salida del programa
        print("Gracias por usar el sistema. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
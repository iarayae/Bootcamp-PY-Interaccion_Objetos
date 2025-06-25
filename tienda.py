from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        self._productos = []

    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo = Producto(nombre, precio, stock)
        for p in self._productos:
            if p == nuevo:
                if isinstance(self, Restaurante):
                    return
                p + nuevo
                return
        if isinstance(self, Restaurante):
            nuevo.modificar_stock(0)
        self._productos.append(nuevo)

    def listar_productos(self):
        salida = f"Productos en {self._nombre}:\n"
        for p in self._productos:
            nombre = p.obtener_nombre()
            precio = p.obtener_precio()
            stock = p.obtener_stock()

            if isinstance(self, Restaurante):
                salida += f"- {nombre} | ${precio}\n"
            elif isinstance(self, Supermercado):
                mensaje_stock = f"{stock}"
                if stock < 10:
                    mensaje_stock += " (Pocos productos disponibles)"
                salida += f"- {nombre} | ${precio} | Stock: {mensaje_stock}\n"
            elif isinstance(self, Farmacia):
                mensaje_precio = f"${precio}"
                if precio > 15000:
                    mensaje_precio += " (Envío gratis al solicitar este producto)"
                salida += f"- {nombre} | {mensaje_precio}\n"
        return salida

    def vender(self, nombre_producto, cantidad):
        for p in self._productos:
            if p.obtener_nombre().lower() == nombre_producto.lower():
                if isinstance(self, Restaurante):
                    pass
                    return True

                elif isinstance(self, Farmacia):
                    if cantidad > 3:
                        print("No se puede vender más de 3 unidades por producto en Farmacias.")
                        return False
                    if p.obtener_stock() <= 0:
                        print("Producto sin stock disponible.")
                        return False
                    vendido = min(p.obtener_stock(), cantidad)
                    p - vendido
                    return True

                elif isinstance(self, Supermercado):
                    if p.obtener_stock() <= 0:
                        print("Producto sin stock disponible.")
                        return False
                    vendido = min(p.obtener_stock(), cantidad)
                    p - vendido
                    return True

        print("Producto no encontrado.")
        return False

class Restaurante(Tienda):
    pass

class Supermercado(Tienda):
    pass

class Farmacia(Tienda):
    pass
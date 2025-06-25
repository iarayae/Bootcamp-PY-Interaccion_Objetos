from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        # Atributos privados
        self._nombre = nombre
        self._costo_delivery = costo_delivery
        # Lista de productos
        self._productos = []

    def ingresar_producto(self, nombre, precio, stock=0):
        # Crear nuevo producto
        nuevo = Producto(nombre, precio, stock)
        for p in self._productos:
            if p == nuevo:
                # Si ya existe, sumar stock (excepto en Restaurante)
                if isinstance(self, Restaurante):
                    return
                p + nuevo
                return
        # Producto nuevo: modificar stock según tipo
        if isinstance(self, Restaurante):
            nuevo.modificar_stock(0)
        self._productos.append(nuevo)
    
    def listar_productos(self):
        salida = f"Productos en {self.__nombre}:\n"
        for p in self._productos:
            nombre = p.obtener_nombre()
            precio = p.obtener_precio()
            stock = p.obtener_stock()

            if isinstance(self, Restaurante):
                # No se muestra stock en restaurantes
                salida += f"- {nombre} | ${precio}\n"

            elif isinstance(self, Supermercado):
                # Mostrar stock, y advertencia si es bajo
                mensaje_stock = f"{stock}"
                if stock < 10:
                    mensaje_stock += " (Pocos productos disponibles)"
                salida += f"- {nombre} | ${precio} | Stock: {mensaje_stock}\n"

            elif isinstance(self, Farmacia):
                # Mostrar precio, con mensaje de envío gratis si corresponde
                mensaje_precio = f"${precio}"
                if precio > 15000:
                    mensaje_precio += " (Envío gratis al solicitar este producto)"
                salida += f"- {nombre} | {mensaje_precio}\n"

        return salida

    def vender(self, nombre_producto, cantidad):
        for p in self._productos:
            if p.obtener_nombre().lower() == nombre_producto.lower():
                if isinstance(self, Restaurante):
                    # Restaurante no modifica stock
                    pass
                elif isinstance(self, Farmacia):
                    if cantidad > 3:
                        return  # Máximo 3 unidades por venta
                    disponible = p.obtener_stock()
                    vendido = min(disponible, cantidad)
                    p - vendido
                elif isinstance(self, Supermercado):
                    # Vender todo lo posible hasta agotar stock
                    disponible = p.obtener_stock()
                    vendido = min(disponible, cantidad)
                    p - vendido
                return

# Subclases de Tienda (herencia)
class Restaurante(Tienda):
    pass

class Supermercado(Tienda):
    pass

class Farmacia(Tienda):
    pass  
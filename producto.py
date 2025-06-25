class Producto:
    def __init__(self, nombre, precio, stock=0):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = max(0, stock)  # Si se ingresa stock negativo, se asigna 0
    
    # Métodos GET: acceder a los atributos privados
    def obtener_nombre(self):
        return self.__nombre

    def obtener_precio(self):
        return self.__precio

    def obtener_stock(self):
        return self.__stock

    # Método SET: solo permite modificar el stock
    def modificar_stock(self, nuevo_stock):
        self.__stock = max(0, nuevo_stock)  # Nunca menor a 0

    # Comparación de productos por nombre (ignora mayúsculas)
    def __eq__(self, other):
        return self.__nombre.lower() == other.__nombre.lower()

    # Suma de productos: suma el stock si el nombre coincide (precio no cambia)
    def __add__(self, other):
        if self == other:
            self.__stock += other.__stock
        return self

    # Resta de stock: utilizado al vender productos
    def __sub__(self, cantidad):
        self.__stock = max(0, self.__stock - cantidad)
        return self
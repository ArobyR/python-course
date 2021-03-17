class Producto:
    contador_producto = 0
    
    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self.__id_producto = Producto.contador_producto
        self.__nombre = nombre
        self.__precio = precio
        
    def __str__(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio} ID: {self.__id_producto}"
    
    def get_precio(self):
        return self.__precio 
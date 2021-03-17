class Orden:
    
    contador_ordenes = 0
    
    def __init__(self, lista_productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = lista_productos
        
    def agregar_producto(self, producto):
        self.__productos.append(producto)
    
    def calcular_total(self):
        precio_total = 0
        for precio_producto in self.__productos:
            precio_total += precio_producto.get_precio()
        
        return precio_total
        
    def __str__(self):
        productos_str = ""
        
        for producto in self.__productos:
            productos_str += f"{producto.__str__()} | "
        
        return f"ID Orden: {self.__id_orden}, Productos: {productos_str}"
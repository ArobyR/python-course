from producto import Producto
from orden import Orden

producto1 = Producto("Mani", 10.00)
producto2 = Producto("Arroz", 20.0)
producto3 = Producto("Atun", 100.00)

producto_random = Producto("Cacao", 20.4)

lista_productos = [producto1, producto2, producto3]

# instanciamos una orden
orden = Orden(lista_productos)
print(orden)
print("Precio total de la orden:", orden.calcular_total())

# agrega nuevo producto
orden.agregar_producto(producto_random)
print("Nuevo total:", orden.calcular_total())

# Orden 2
producto4_orden2 = Producto("Verduras", 30)
lista_productos = [producto4_orden2]
orden2 = Orden(lista_productos)
print(orden2)
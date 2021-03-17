# no puedes reasignar valores
frutas = ("Mango", "Manzana", "Pera")

print(type(frutas))

frutas_lista = list(frutas)
frutas_lista[0] = "Manguito"
frutas = tuple(frutas_lista)
print(frutas, end=", ")

# no podemos agregar ni eliminar elementos de una tupla
del frutas
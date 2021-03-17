'''set es una collecion sin orden y sin indices, no permite 
elmentos y los elementos no se pueden modificar, pero si agregar nuevos
o eliminar
'''
planetas = {"Marte", "Jupiter", "Venus"}

print(planetas)

# revisar si un elemento esta presente
print("Tierra" in planetas)

# agregar
planetas.add("Tierra")
print(planetas)

# eliminar
planetas.remove("Jupiter")
print(planetas)

# no arroja excepcion con discard
planetas.discard("Martes")

#limpiar el set 
planetas.clear()
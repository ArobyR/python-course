diccionario = {
    "Tesla": "Model 3",
    "Amazon": "Amazon basics",
    "Develop AI": "Big AI"
}

print(len(diccionario))

# accediento a un elemento
print(diccionario["Amazon"])
print(diccionario.get("Develop AI"))

# modificando valores
diccionario["Develop AI"] = "The biggest AI"
print(diccionario)

# iterar
for termino in diccionario:
    print(diccionario[termino])
for valor in diccionario.values():
    print(valor)

print("_______________________________")
for llave, valor in diccionario.items():
    print(llave, valor)
    
# agregar nuevos elementos
diccionario["PK"] = 22
print(diccionario)

# remover elementos 
diccionario.pop("PK")

# limpiar
diccionario.clear()
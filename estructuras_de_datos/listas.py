example = [1, 2, 3, 4, 5]

example.append("new")
example.insert(1,"first")
print(id(example[0]))
print(id(example[1]))

print(len(example[1]))

# imprimir rango
print(example[0:2]) # 0 - 1

#imprimir hasta el indice final 
print(example[:3]) # sin incluir el tres

#incide especificado hasta el final
print(example[1:]) # sin incluir el tres

#remover elemento
example.remove("new")
print(example)
# remover ultimo elemento
example.pop()
print(example)

# remover el indice indicado
del example[0]
print(example)

# limpiar los elementos 
example.clear()
print(example)

# eliminar nombre por completo
del example
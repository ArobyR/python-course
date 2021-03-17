# alto = int(input("Proporciona el alto:"))
# ancho = int(input("Proporciona el ancho:"))

# area = alto * ancho
# perimetro = (alto * ancho) * 2

# print("Area: ", area)
# print("Perimetro: ", perimetro)

# El usuario proporcionará un valor entre 0 y 10.

# Si está entre 9 y 10: imprimir una A

# Si está entre 8 y menor a 9: imprimir una B

# Si está entre 7 y menor a 8: imprimir una C

# Si está entre 6 y menor a 7: imprimir una D

# Si está entre 0 y menor a 6: imprimir una F

# cualquier otro valor debe imprimir: Valor desconocido

calification = int(input('Introduce la calificacion: '))

if calification == 9 or calification == 10:
    print("A")
elif calification == 8:
    print("B")
elif calification == 7:
    print("C")
elif calification == 6:
    print("D")
elif calification == 0 or calification < 6:
    print("F") 

# for i in range(1, 11):
#     print(i)
    
# count = 0

# while count < 10:
#     count += 1
#     print(count)


numbers = (13, 1, 8, 3, 2, 5, 8)
numbers_list = []
for numero in numbers:
    if numero < 5:
        numbers_list.append(numero)
        
print(numbers_list)
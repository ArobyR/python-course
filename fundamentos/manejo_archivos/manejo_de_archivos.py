def get_nombre(nombre):
    return nombre


try:
    archivo = open("archivo.txt", "w")
    hola = "hola mundo"
    archivo.write(get_nombre("Aaron Stone\n"))
    print("Agregado sin salto de linea", file=archivo)
    print("Funciona con rutas absolutas y relativas", file=archivo)
    archivo.write("Adios")
    
except Exception as e:
    print(e)
finally:
    archivo.close()
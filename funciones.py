# parametros es una variable definida dentro de la definicion de la funcion
# argumentos es valor enviado a la funcion

def suma(value1 = 0, value2 = 0):
    """ 
    Esta funcion suma dos numeros
    recibiendo dos valores por argumento
    Proceso de ejecucion
    definicion
    llamada
    pase por argumentos
    ejecucion
    
    """
    return value1 + value2

print(suma.__doc__)
print(suma(22, 11))
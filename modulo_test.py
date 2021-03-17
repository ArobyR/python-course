from modulos import modulo_aritmetica as aritmetica # importacion de todo el archivo
from modulos.modulo_persona.persona import Persona # importa solo la clase 
# import modulos.modulo_aritmetica as aritmetica
# import {} from carpeta
resultado = aritmetica.sumar(1, 2)
print(resultado)

persona = Persona("Elliot", 36)
print(persona)
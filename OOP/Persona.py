class Persona:
    
    """self es como un this crea e inicializa el atributo"""
    """ Los parametros del constructor son opcionales, podemos inicialos
        dentro
    """
    def __init__(self, nombre, edad = None):
        self.nombre = nombre
        self.edad = edad 

    def imprimir_nombre(self):
        print(self.nombre)
    

# Modificar los valores
Persona.nombre = "Pepito"
Persona.edad = 28

# Acceder a los valores, no se instancia objetos
print(Persona.nombre)
print(Persona.edad)

# Creacion de un objeto
persona = Persona("Juana", 28)
persona.imprimir_nombre()

example = Persona("Stonks")
example.imprimir_nombre()
print(example.edad)
class Persona:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__edad = 20
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, name):
        self.__nombre = name
    
#obj__class__variable tecnicamente no pasarlo por el constructor    
persona = Persona("Gente")
print(persona.get_nombre())
persona.__nombre = "Cambio..." # podria ser una instancia de clase general y no del obj
print(persona.__nombre)
print(persona.get_nombre())
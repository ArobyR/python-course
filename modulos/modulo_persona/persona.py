class Persona:
    
    def __init__(self, nombre_, edad_):
        self.nombre = nombre_
        self.edad = edad_

    def __str__(self):
        return "Nombre: {nombre} Edad: {edad}".format(nombre=self.nombre, edad=self.edad)
    
class Vehiculo:
    pass
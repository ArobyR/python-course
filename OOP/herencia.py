class Persona:
    
    def __init__(self, nombre_, edad_):
        self.nombre = nombre_
        self.edad = edad_

    def __str__(self):
        '''__str__ clase general que imprime la direccion en memoria, 
            pero podemos sobre escribirlo
        '''
        return "Nombre: {nombre} Edad: {edad}".format(nombre=self.nombre, edad=self.edad)
    
class Empleado (Persona):
    
    def __init__(self, nombre_, edad_, sueldo):
        super().__init__(nombre_, edad_)
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + ' Sueldo ' + str(self.sueldo)
    
    def imprime_sueldo(self):
        print(self.sueldo)
                   
persona = Persona("GG", 22)
print(persona)

empleado = Empleado("Dolores", 22, 1000.01)
empleado.imprime_sueldo()

print(empleado)
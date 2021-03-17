from empleado import Empleado

class Gerente(Empleado):
    
    def __init__(self, nombre_, sueldo_, departamento_):
        super().__init__(nombre_, sueldo_)
        self.departamento = departamento_
        
    def __str__(self):
        return super().__str__() + " Departamento: " + self.departamento
class Empleado:
    
    def __init__(self, nombre_, sueldo_):
        self.nombre = nombre_
        self.sueldo = sueldo_
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Sueldo: {self.sueldo}"
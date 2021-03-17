class Vehiculo:
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "Color: {color} ruedas: {ruedas}".format(color=self.color, ruedas=self.ruedas)
    
    
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        
    def __str__(self):
        return super().__str__() + ' velocidad: ' + str(self.velocidad) + ' km/hr'
    

class Bicicleta(Coche):
    
    def __init__(self, color, ruedas, velocidad, tipo):
        super().__init__(color, ruedas, velocidad)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + ' tipo: ' + self.tipo

    
obj_vehiculo = Vehiculo("Verde", 4)
print(obj_vehiculo)

obj_coche_t = Coche("Naranja", 4, 200)
print(obj_coche_t)

obj_bicicleta = Bicicleta("Rojo", 2, 70, "urbana")
print(obj_bicicleta)
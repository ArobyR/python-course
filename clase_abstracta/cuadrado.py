from figura_geometrica import FiguraGeometrica 
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self):
        FiguraGeometrica.__init__(self)
        # super().__init__(ancho, alto)
        Color.__init__(self)
    
    def area(self):
        return self.get_alto() * self.get_ancho()
        
    def __str__(self):
        return FiguraGeometrica.__str__(self) + Color.__str__(self) + ' El area es: ' + str(self.area())

    
cuadrado = Cuadrado()
print(cuadrado)
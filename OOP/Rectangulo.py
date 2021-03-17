class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def get_area(self):
        return self.base * self.altura

rectangulo = Rectangulo(20, 10)
print(rectangulo.get_area())
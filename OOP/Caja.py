class Caja:
    
    def __init__(self, alto = 0, ancho = 0, largo = 0):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        
    def set_alto(self):
        self.alto = int(input("Proporcione el alto: "))
    
    def set_ancho(self):
        self.ancho = int(input("Proporcione el ancho: "))
    
    def set_largo(self):
        self.largo = int(input("Proporcione el largo: "))
        
    def get_volumen(self):
        return self.alto * self.ancho * self.largo
    
    
caja_master = Caja()
caja_master.set_alto()
caja_master.set_ancho()
caja_master.get_largo()

print("Volumen: " + caja_master.get_volumen())
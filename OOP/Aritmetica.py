class Aritmetica:
    
    def __init__(self, operando, operando2):
        self.operando = operando
        self.operando2 = operando2
    
    def sumar(self):
        return self.operando + self.operando2
    
    def multiplicacion(self):
        return self.operando * operando2
    
    def resta(self):
        return self.operando - self.operando2
    
    def division(self):
        if self.operando2 == 0:
            return "No se puede dividir por cero"
        return self.operando / self.operando2
    
    
arit = Aritmetica(2)
print(arit.sumar())
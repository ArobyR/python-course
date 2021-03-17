class MiClase:
    
    variable_estatica = "Hi world" # variable de clase
    
    def __init__(self, variable_instancia):
        self.variable_inst = variable_instancia


miclase = MiClase("Variable instanciada")

print(MiClase.variable_estatica)
print(miclase.variable_inst)

# podemos acceder de a las variables de clases desde los objetos
print(miclase.variable_estatica)

'''tendriamos que hacer una modificacion para que la variable de instancia se asocie con la 
clase, ejemplo: Miclase.variable_instancia = "Say hi"
si lo hacemos con el objecto esa modificacion solo se asocia con ese objeto
no es una buena practica'''

# esta variable solo se asocia al objeto (se crea una nueva)
miclase.variable_estatica = "Otro valor" 
# en cambio esta variable se asocia con la clase (modifica el valor globalmente)
MiClase.variable_estatica = "Cambio..."  

print(miclase.variable_estatica)
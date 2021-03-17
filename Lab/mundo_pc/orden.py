class Orden:
    
    contador_ordenes = 0
    
    def __init__(self):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__computadoras = []
        
    def agregar_computadoras(self, object_array_computers):
        self.__computadoras = object_array_computers
    
    def get_computadoras(self):
        print(self.__computadoras)
    
    def __str__(self):
        
        str_computadoras = ""
        for computadora in self.__computadoras:
            str_computadoras += f"{computadora.__str__()}"
            
        return f"Orden: {self.__id_orden} computadoras:\n {str_computadoras}"
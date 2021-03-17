class Persona:
    '''__usuario = False
    _protegido
    __privado
    '''
    def __init__(self, nombre_, apellido):
        self.nombre = nombre_
        self._apellido = apellido
        self.__usuario = False
        
    def __metodo_privado(self):
        print("Nombre " + self.nombre, end=", " )
        print("Apellido " + self._apellido)
    
    def publico(self):
        self.__metodo_privado();
    

persona = Persona("FuiFui", "Santos")

persona.publico()
persona.__metodo_privado()    
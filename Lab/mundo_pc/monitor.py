class Monitor:
    
    contador_monitores = 0
    
    def __init__(self):
        Monitor.contador_monitores += 1
        self.__id_monitor = Monitor.contador_monitores
        self.__marca = ""
        self.__tamanio = ""

    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca_):
        self.__marca = marca_
        
    def get_tamanio(self):
        return self.__tamanio
    
    def set_tamanio(self, tamanio_):
        self.__tamanio = tamanio_
        
    def __str__(self):
        return f"Monitor: Id: {self.__id_monitor}, marca: {self.__marca}, tamanio: {self.__tamanio} \n"
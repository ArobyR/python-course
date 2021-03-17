from raton import Raton
from teclado import Teclado
from monitor import Monitor

class Computadora:
    
    contador_computadoras = 0
    
    def __init__(self):
        Computadora.contador_computadoras += 1
        self.__id_computadora = Computadora.contador_computadoras
        self.__nombre = ""
        self.__monitor = None
        self.__teclado = None
        self.__raton = None
        
    
    def get_nombre_computadora(self):
        return self.__nombre
    
    def set_nombre_computadora(self, nombre_):
        self.__nombre = nombre_
    
    def get_monitor(self):
        return self.__monitor
    
    def set_monitor(self, obj_monitor):
        self.__monitor = obj_monitor
    
    def get_teclado(self):
        return self.__teclado
    
    def set_teclado(self, obj_teclado):
        self.__teclado = obj_teclado
    
    def get_raton(self):
        return self.__raton
    
    def set_raton(self, obj_raton):
        self.__raton = obj_raton    
        
    def __str__(self):
        return f'''{self.__nombre}, Id: {self.__id_computadora}
        {self.__monitor.__str__()} 
        {self.__teclado.__str__()} 
        {self.__raton.__str__()} \n'''
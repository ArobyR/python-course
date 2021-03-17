# ABSTRACT BASE 
# No nos permite instanciar objetos
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    
    def __init__(self):
        # instance attributes
        self.__ancho = 0
        self.__alto = 0
    
    def get_alto(self):
        """No se deberia implementar el metodo
           pero es solo para testiar
        """
        return self.__alto
    
    def get_ancho(self):
        """No se deberia implementar el metodo
           pero es solo para testiar
        """
        return self.__ancho
    
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return f"El alto: {self.__alto}, ancho: {self.__ancho} \n"
class FiguraGeometrica:
    
    def __init__(self):
        # instance attributes
        self.__ancho = 0
        self.__alto = 0
    
    def get_alto(self):
        return self.__alto
    
    def set_alto(self, alto):
        self.__alto = alto
    
    def get_ancho(self):
        return self.__ancho
    
    def set_ancho(self, ancho):
        self.__ancho = ancho
    
    def __str__(self):
        return f"Ancho: {self.__ancho} Alto: {self.__alto} "
        # return 'Ancho: {ancho} Alto: {alto}'.format(ancho=self.__ancho, alto=self.__alto)    
from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    
    contador_ratones = 0
    
    def __init__(self):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        
    def __str__(self):
        return f"Raton: Id: {self.__id_raton}, marca: {self._marca}, tipo entrada: {self._tipo_entrada} \n"
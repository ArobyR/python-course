from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    
    contador_teclados = 0
    
    def __init__(self):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
    
    def __str__(self):
        return f"Teclado: Id: {self.__id_teclado}, marca: {self._marca}, tipo entrada: {self._tipo_entrada} \n"
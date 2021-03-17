class DispositivoEntrada:
    
    def __init__(self):
        self._tipo_entrada = ""
        self._marca = ""
    
    def get_tipo_entrada(self):
        return self._tipo_entrada
    
    def set_tipo_entrada(self, tipo_entrada_):
        self._tipo_entrada = tipo_entrada_
        
    def get_marca(self):
        return self._marca
    
    def set_marca(self, marca_):
        self._marca = marca_
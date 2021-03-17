class Pelicula:
    
    def __init__(self):
        self.__nombre = ""
        
    def set_nombre_pelicula(self, nombre_):
        self.__nombre = nombre_
        
    def get_nombre_pelicula(self):
        return self.__nombre
        
    def __str__(self):
        return f"Nombre pelicula: {self.__nombre}"  
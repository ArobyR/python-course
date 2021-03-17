class Color:
    
    def __init__(self):
        self.__color = None    
        
    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color
        
    def __str__(self):
        return f"Color: {self.__color}"
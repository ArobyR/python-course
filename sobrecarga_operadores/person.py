class Person:
    
    def __init__(self, name_):
        self.__name = name_
    
    # metodo sobreescrito de la clase padre object
    def __add__(self, another_object):
        return self.__name + " " + another_object.__name
    
    def __sub__(self, another_object):
        return f"{another_object.__name}, This isn't support"
    
person1 = Person("Jimena")
person2 = Person("Strange")

# una nueva forma de trabajar al operador +
print(person1 + person2)
class MiClase:
    
    """
    No se asocia a ningun objecto, por ende no recibe
    self, los metodos estaticos no pueden acceder a variables
    de instancias.
    El parametro de self hace referencia a instancias
    de la clase
    """
    variable_clase = "Variable de clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instanciada"
    
    @staticmethod
    def metodo_esttico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        
        # desde un metodo estatico no podemos acceder a una variable de intancia
        #print(Miclase.variable_instancia)
    
    @classmethod
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
        # no podemos acceder a las variables de instancia desde el contexo estatico
        #print(cls.variable_clase)

    def metodo_instancia(self):
        print(self.variable_instancia)
        print(self.variable_clase)

MiClase.metodo_esttico()
MiClase.metodo_clase()

# el contexto estatico no puede acceder al contexto dinamico, pero el contexto dinamico si puede puede acceder al estatico 
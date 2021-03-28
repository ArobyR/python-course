class Person:
    
    def __init__(self):
        self.id_persona = 0
        self.nombre = ""
        self.apellido = ""
        self.email = ""
    
    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona_):
        self.id_persona = id_persona_
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre_):
        self.nombre = nombre_
        
    def get_apellido(self):
        return self.apellido
    
    def set_apellido(self, apellido_):
        self.apellido = apellido_
    
    def get_email(self):
        return self.email
    
    def set_email(self, email_):
        self.email = email_
        
    def __str__(self):
        return f'{self.id_persona} {self.nombre} {self.apellido} {self.email}'
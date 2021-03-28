import pg

class Conexion:
    
    DATABASE = ''
    USERNAME = ''
    PASSWORD = ''
    DB_PORT = ''
    HOST = ''
    conexion = get_conexion()
    cursor = get_cursor()
    
    @classmethod
    def get_conexion(cls):
        pass    
    
    @classmethod
    def get_cursor(cls):
        pass
    
    @classmethod
    def close_conexion(cls):
        pass
    
    def __init__(self):
        pass
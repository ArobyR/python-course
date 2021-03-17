class NumerosNoParesException(Exception):
    
    """ Overwrite the property message """
    def __init__(self, msg):
        self.message = msg   
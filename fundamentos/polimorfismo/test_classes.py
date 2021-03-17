from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto, end="\n\n")
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
   
obj_empleado = Empleado("Nombrado", 5000.20)
obj_gerente = Gerente("Gerente", 50020, "Tecnologia")
    
imprimir_detalles(obj_empleado)
imprimir_detalles(obj_gerente)
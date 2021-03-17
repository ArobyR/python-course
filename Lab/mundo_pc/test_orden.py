from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden

raton = Raton()
raton.set_marca("Logic Tech")
raton.set_tipo_entrada("USB")

monitor = Monitor()
monitor.set_marca("Dell")
monitor.set_tamanio("27 pulgadas")

teclado = Teclado()
teclado.set_marca("Annie")
teclado.set_tipo_entrada("WI-FI")

primera_computadora = Computadora()
primera_computadora.set_nombre_computadora("Aero")
primera_computadora.set_monitor(monitor)
primera_computadora.set_raton(raton)
primera_computadora.set_teclado(teclado)    


raton2 = Raton()
raton2.set_marca("Lenovo")
raton2.set_tipo_entrada("Bluethoo")

monitor2 = Monitor()
monitor2.set_marca("Alienware")
monitor2.set_tamanio("32 pulgadas")

teclado2 = Teclado()
teclado2.set_marca("Asus")
teclado2.set_tipo_entrada("USB")

second_computadora = Computadora()
second_computadora.set_nombre_computadora("Asus")
second_computadora.set_monitor(monitor2)
second_computadora.set_raton(raton2)
second_computadora.set_teclado(teclado2)    

lista_computadoras = [primera_computadora, second_computadora]

orden = Orden()
orden.agregar_computadoras(lista_computadoras)
print(orden)
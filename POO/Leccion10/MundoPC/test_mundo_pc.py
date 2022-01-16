from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
from Orden import Orden

teclado1 = Teclado('HP', 'USB')
raton1 = Raton('Logitech', 'USB')
monitor1 = Monitor('HP', 22)
computadora1 = Computadora('HP 15', monitor1, teclado1, raton1)

teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', 19)
computadora2 = Computadora('ACER', monitor2, teclado2, raton2)

teclado3 = Teclado('Razer', 'USB')
raton3 = Raton('Razer', 'USB')
monitor3 = Monitor('MSI', 27)
computadora3 = Computadora('NBOX Gaming', monitor3, teclado3, raton3)


computadoras1 = [computadora1, computadora2] 
orden1 = Orden(computadoras1)
print(orden1)
orden1.agregar_computadora(computadora3)
print(orden1)

computadoras2 = [computadora3, computadora1] 
orden2 = Orden(computadoras2)
print(orden2)
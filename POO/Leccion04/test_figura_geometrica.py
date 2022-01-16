from FiguraGeometrica import FiguraGeometrica
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

print('Creación Objeto cuadrado'.center(50,'-'))

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

cuadrado1 = Cuadrado(lado=5, color='rojo')
# print(cuadrado1.ancho)
# print(cuadrado1.alto)
print(f'Área del cuadrado = {cuadrado1.calcularArea()} ')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=11, alto=6, color='verde')
print(f'Área del rectángulo = {rectangulo1.calcularArea()} ')
print(rectangulo1)

# MRO - Method Resolution Order - Orden de jerarquía seguido por las clases
print('MRO'.center(50,'-'))
print(Cuadrado.mro())
print(Rectangulo.mro())
print('Fin'.center(50,'-'))
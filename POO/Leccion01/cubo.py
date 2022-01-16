class Cubo:
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
    
    def calcularVolumen(self):
        return self.ancho * self.profundidad * self.altura

ancho = float(input('Proporciona la base: '))
profundidad = float(input('Proporciona la profundidad: '))
altura = float(input('Proporciona la altura: '))

cubo1 = Cubo(ancho,altura,profundidad)
print(f'Volumen cubo: {cubo1.calcularVolumen()}')
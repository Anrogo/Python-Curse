# Generadores
# Es una función especial que retorna valores, producidos en una secuencia, poco a poco
# Suspende la ejecución de la función yield (producir) y no usa return

def generador():
    yield 1
    print('Se reanuda la ejecución')
    yield 2
    print('Se reanuda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()

# Con cada llamada consumimos un valor, un yield, diferente
print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir más valores de los que produce el generador,
# lanza un error de StopIteration puesto que hay que regenerarlo cada vez

# Consumiendo los valores con un ciclo for automáticamente
for valor in generador():
    print(f'Número generado: {valor}')
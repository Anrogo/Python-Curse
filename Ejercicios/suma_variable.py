def sumaVariable(*args):
    suma = 0
    for n in args:
        suma += n
    print(f'Resultado de la suma: {suma}')

#sumaVariable(1,2,3)

def productoVariable(*args):
    resultado = 1
    for n in args:
        resultado *= n
    print(f'Resultado de la suma: {resultado}')


productoVariable(3,7,2)
productoVariable(3,2)
# Profundizando en tuplas

# Declarar variables
a, b = 'Hola', 'Adios' # Tupla a la que le hacemos unpacking
print(a,b)
# swap (intercambio)
a, b = b, a
print(a,b)

# Regresar múltiples valores en una función
def minmax(elementos):
    return min(elementos), max(elementos)

min, max = minmax([1,2,3,4,5])
print(f'Valor min: {min}, Valor max: {max}')

# Regresar la suma de una tupla (2 maneras diferentes con el mismo resultado)
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')
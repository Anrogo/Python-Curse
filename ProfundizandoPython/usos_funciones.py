# Las funciones en python son ciudadanas de primera clase
# First class citizens

def sumar(a, b):
    return a + b

# 1. Asignar una función a una variable (no se usan paréntesis)
mi_funcion = sumar

# Llamamos la función a través de la variable asignada
resultado = mi_funcion(5,8)
print(resultado)

# 2. Función como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar {sumar_arg(a, b)}')

operacion(4,3, sumar)

# 3. Podemos retornar una función desde dentro de otras funciones
def retornar_funcion():
    # Retornamos una función
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado función retornada: {mi_funcion_retornada(5,7)}')
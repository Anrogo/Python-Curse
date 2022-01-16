# Decoradores
# Un decorador es una función que recibe una función y regresa otra
# Lo vamos a utilizar para extender funcionalidad
# 1. Función decoradora (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la función')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Después de ejecutar la función\n')
        return resultado

    return funcion_decorada_c


@funcion_decorador_a
def sumar(a, b):
    return a + b


resultado = sumar(3, 2)
print(f'Resultado de la suma: {resultado}\n')

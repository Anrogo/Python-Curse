# Decoradores
# Un decorador es una función que recibe una función y regresa otra
# Lo vamos a utilizar para extender funcionalidad
# 1. Función decoradora (a)
# 2. Función a decorar (b)
# 3. Función decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c():
        print('Antes de ejecutar la función')
        funcion_a_decorar_b()
        print('Después de ejecutar la función\n')

    return funcion_decorada_c

# Definimos una función y vamos a extender su funcionalidad con un decorador
@funcion_decorador_a
def mostrar_mensaje():
    print('Hola desde función mostrar mensaje')

mostrar_mensaje()

# Y se puede añadir en cualquier función que queramos
@funcion_decorador_a
def imprimir():
    print('Hola desde función imprimir')

imprimir()
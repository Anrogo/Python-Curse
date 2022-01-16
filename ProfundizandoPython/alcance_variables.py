# Alcance de Variables (scope)

# Definición de variable global
var_global = 'Variable global'

def imprimir():
    # Acceder a una variable global
    global var_global
    var_global = 'Nuevo valor'
    print(f'Variable global desde función: {var_global}')

    # Definición de variable local
    var_local = 'Variable local'
    print(f'Variable local desde función: {var_local}')


    def funcion_anidada():
        print(f'Variable local dentro de función anidada: {var_local}')

    funcion_anidada()

imprimir()
print(f'Variable global fuera de la función: {var_global}')
# No es posible acceder a variables locales
# fuera del bloque que se definieron
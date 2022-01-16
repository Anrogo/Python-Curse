# Un closure es una función que define a otra, y además de regresar
# la función anidada puede acceder a las variables locales definidas
# en la función principal externa

# Función principal
def operacion(a, b):
    # Definimos una función interna o anidada
    def sumar():
        return a + b

    #Retornar la función
    return sumar

mi_funcion_closure = operacion(5,2)
print(f'Resultado de la función closure: {mi_funcion_closure()}')


# Llamar a la función regresada al vuelo
print(f'Resultado de la función closure al vuelo: {operacion(2,3)()}')

# Función principal
def operacion(a, b):
    # 1. Definimos una función lambda interna o anidada y la retornamos
    return lambda: a + b

# La ejecución es exactamente la misma que antes. Solo cambia la estructura interna que le damos
print(f'Resultado de la función closure al vuelo: {operacion(7,4)()}')

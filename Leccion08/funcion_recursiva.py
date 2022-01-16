# Una función recursiva consiste en una función que se llama así misma, en bucle, hasta completar una cierta tarea
# Ejemplo clásico: factorial de un número
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120
def factorial(numero):
    if numero == 1:
        return 1
    else:
        # Regresamos el cálculo del mismo número por el resultado de la misma multiplicación restándole 1 cada vez a ese número
        return numero * factorial(numero-1)

numero = 5
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')
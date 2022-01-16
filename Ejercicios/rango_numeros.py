#valor = int(input("Introduce un valor numérico: "))

valorMin = 0
valorMax = 5

#rango = ( valor >= valorMin ) and (valor <= valorMax)

# Operador ternario:

#print(f'El valor {valor} está dentro de rango.') if rango else print(f'El valor {valor} está fuera de rango.')

'''
if rango:
    print(f'El valor {valor} está dentro de rango.')
else:
    print(f'El valor {valor} está fuera de rango.')
'''


# Ciclo While
cont = 5
while cont > 0:
    print(cont)
    cont -= 1
print('Fin ciclo while')

# Ciclo for:
cadena = 'Hola'

for letra in cadena:
    print(letra)
print('Fin ciclo for')

cadena = 'Holanda'

for letra in cadena:
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
else:
    print('Fin ciclo for')

""" for i in range(6):
    if i % 2 == 0:
        print(f'Valor: {i}') """

for i in range(6):
    if i % 2 != 0:
        continue
    print(f'Valor: {i}')
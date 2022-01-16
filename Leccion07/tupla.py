# Definir una tupla
frutas = ('Naranja', 'Plátano', 'Guayaba')

# Saber la longitud:
print(len(frutas))

# Acceder a un elemento:
print(frutas[-1])

# Acceder a un rango:
print(frutas[0:])

# Cambiar valor tupla. Convirtiendo la tupla a lista, modificando la lista y volviendo a convertir de lista a tupla
frutaLista = list(frutas)
frutaLista[0] = 'Pera'
frutas = tuple(frutaLista)

print('\n')
# Iterar la tupla:
for fruta in frutas:
    print(fruta, end=' ')

print('\n')

# Para eliminar la tupla por completo: 
# del frutas
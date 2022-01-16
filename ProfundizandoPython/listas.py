# Profundizando listas
# Listas son mutables []
nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura María Gonzalo Ernesto'.split()

# Sumar listas
print(f'Sumar listas: {nombres1 + nombres2}')

# Extender una lista sobre otra lista. El resultado es similar a sumarlas
nombres1.extend(nombres2)
print(f'Extender lista1: {nombres1}')

# Lista de números
numeros1 = [10, 40, 15, 4, 20, 90, 4]
# obtener el índice del primer elemento encontrado en una lista
# help(list.index)
print(f'Indice 4: {numeros1.index(4)}')

# Invertir orden elementos de una lista:
numeros1.reverse()
print(f'Lista invertida: {numeros1}')

# Ordenar los elementos de una lista
numeros1.sort()
print(f'Lista ordenada (ascendente): {numeros1}')

# Ordenada de forma descendente:
numeros1.sort(reverse=True)
print(f'Lista ordenada (descendente): {numeros1}')

# Obtener el valor mín y máx de una lista
print(f'Valor mínimo: {min(numeros1)}')
print(f'Valor máximo: {max(numeros1)}')

# Copiar los elementos de una lista (las referencias de cada objeto en memoria). Coincide el contenido únicamente..
numeros2 = numeros1.copy()
print(numeros2)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Podemos usar el constructor de la lista:
numeros2 = list(numeros1)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Y otra forma de copiar los elementos es utilizar Slicing:
numeros2 = numeros1[:]
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido? {numeros1 == numeros2}')

# Multiplicación de listas
lista_multiplicacion = 5*[[2,5]]
print(lista_multiplicacion)
# En este caso todos los objetos serán idénticos en referencia y en valor
print(f'Misma referencia: {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido: {lista_multiplicacion[0] == lista_multiplicacion[1]}')
# Y si modificamos uno se modifican todos, por lo que comprobaríamos lo anterior
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# Matrices en Python. Es una lista de listas, anidadas unas dentro de otras
matriz = [[10,20], [30,40,50],[60,70,80,90]]
print(f'Matriz original: {matriz}')
# Para recuperar un elemento concreto necesitamos el primer índice y luego el segundo, el subíndice a su vez
print(f'Fila 0, Columna 0: {matriz[0][0]}')
print(f'Fila 2, Columna 2: {matriz[2][2]}')
matriz[2][0] = 65
print(f'Matriz modificada: {matriz}')

# Ordenamiento de matrices
lista_listas = [
    [10,14,87,90,71],
    [4,5,6,7],
    [9,0,11,15,45,61,70]
]

# Ordenamos en función del largo:
lista_listas.sort(key=len)
print(f'Ordenar lista: {lista_listas}')

# Ordenamiento utilizando cadenas: sorted built-in
# help(sorted)
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
# Para ordenar los elementos de esta lista de manera descendente (z - a):
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)
# Ordenar por la cantidad de caracteres de cada elemento (- a +)
nombres1 = sorted(nombres1, key=len)
print(nombres1)

# Built-in reversed. Idéntico resultado que antes pero al revés
nombres1 = reversed(nombres1)
print(list(nombres1))
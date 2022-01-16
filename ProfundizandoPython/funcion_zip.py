# Clases y métodos disponibles en Python
# print(dir(__builtins__))
# help(zip)
# La longitud de la lista más pqueña marca el número límite de elementos que se van a iterar y mezclar
numeros = [1,2,3]
letras = ['a','b','c','d']
ids = 321,322,323,324,325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros,letras,ids,conjunto)
print(list(mezcla))
#print(tuple(zip(numeros,letras,identificadores)))
#print(type(mezcla))

# Iterar en paralelo:
for numero, letra, id, aleatorio in zip(numeros,letras,ids, conjunto):
    print(f'Número: {numero}, Letra: {letra}, Id:{id}, Aleatorio:{aleatorio}')
    
nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros,letras,ids, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')

print(nueva_lista)

# Unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
print(mezcla)
numeros, letras = zip(*mezcla)
print(f'Números: {numeros}, Letras: {letras}')

# Ordenamiento
letras = ['c','a','e','b','d']
numeros = [3, 2, 4, 1, 0]
mezcla = zip(letras, numeros)
# Sin orden:
print(tuple(mezcla))
# Ordenado por letra (primer iterable)
print(sorted(zip(letras, numeros)))
# Y si lo ordenamos por números:
print(sorted(zip(numeros, letras)))

# Crear un diccionario con zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento de un diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave,nueva_edad))
print(diccionario)

# Para añadir nuevos elementos sería de la misma manera solo que poniendo un valor que no exista en el diccionario
llave = ['Email']
valor = ['jperez@email.com']
diccionario.update(zip(llave,valor))
print(diccionario)
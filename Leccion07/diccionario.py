# Declaramos el diccionario, que tiene una key-value o también se puede decir como clave/llave y un valor vinculado a ésta
diccionario = {
    'IDE':'Integrated Development Enviroment',
    'OOP':'Object Oriented Programming',
    'DBMS':'Database Management System'
}

print(diccionario)

# Longitud del diccionario:
print(len(diccionario))

# Acceder a un elemento (key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento (get)
print(diccionario.get('OOP'))

# Modificar elementos del diccionario:
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

# Iterar un diccionario con sus dos atributos:
for clave, valor in diccionario.items():
    print(clave, valor)

# Iterar para mostrar solo la clave o key:
for clave in diccionario.keys():
    print(clave)

# Iterar para mostrar solo el valor o value:
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de algún elemento (respetando mayús):
print('IDE' in diccionario)

# Agregar un nuevo elemento (la clave debe ser diferente):
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Borrar un elemento:
diccionario.pop('DBMS')
print(diccionario)

# Limpiar el diccionario sin borrar la variable como tal
diccionario.clear()
print(diccionario)

# Y para eliminar el diccionario
del diccionario
#print(diccionario) #da error
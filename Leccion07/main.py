# Definir una lista de tipo str
nombres = ['Juan', 'Karla', 'Ricardo', 'María']

# Imprimir la lista de nombres:
print(nombres)

# Para acceder al último valor de la lista:
print(nombres[-1])

# Imprimir un rango:
print(nombres[0:2])

# Recorrer la lista sin pasar por el primer valor:
print(nombres[:3])

# Recorrer la lista desde el índice indicado hasta el final:
print(nombres[1:])

# Cambiar un valor:
nombres[3] = 'Ivone'
print(nombres)

# Iterar la lista:
cont = 0
for nombre in nombres:
    cont += 1
    print(f'Nombre {cont}: {nombre}')
else:
    print('No exiten más nombres en la lista')
    
# Preguntar la longitud de una lista:
print(len(nombres))

# Agregar nuevo elemento a la lista:
nombres.append('Lorenzo')
print(nombres)

# Insertar un elemento en un índice específico:
nombres.insert(1, 'Octavio')
print(nombres)

# Eliminar un elemento:
nombres.remove('Octavio')

# Eliminar el último valor agregado (al final)
nombres.pop()
print(nombres)

# Eliminar un índice
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
#print(nombres) #No podemos acceder y dará error!
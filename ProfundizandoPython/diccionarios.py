# Profundizando en diccionarios

# Los dic guardan un orden (a diferencia de un set)
diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)

# Los dic son mutables, pero las llaves deben ser inmutables. Solo podremos utilizar tuplas como llaves
# diccionario = {[1,2]:'Hola'}
#diccionario2 = {(1,2):'Hola'}
#print(diccionario)

# Se agrega una llave si no se encuentra
#diccionario2['Departamento'] = 'Sistemas'
#print(diccionario)

# No hay valores duplicados en las llaves de un diccionario. Las llaves deben ser únicas (si ya existe se reemplaza)
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# Recuperar un valor indicando una llave
print(diccionario['Nombre'])

# El método get recupera  una llave, y si no existe NO lanza una excepción
# Además podemos regresar un valor en el caso de que no exista la llave
print(diccionario.get('Nombres', 'No se encontró la llave'))
print(diccionario)

# setdefault sí modifica el diccionario, además se puede agregar un valor por defecto
nombre = diccionario.setdefault('Nombres', 'Valor por defecto')
print(nombre)
print(diccionario)

# Imprimir con pprint. Impresión mejorada del diccionario
from pprint import pprint as pp
pp(diccionario, sort_dicts=False)
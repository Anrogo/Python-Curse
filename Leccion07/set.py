# set (no tiene un orden fijo y utiliza llaves)
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)

# Comprobar si un elemento está presente
print('Marte' in planetas)

# Agregar un nuevo elemento
planetas.add('La Tierra')

# No se pueden duplicar elementos.. Es como si no hubiéramos hecho nada
planetas.add('La Tierra')
print(planetas)

# Eliminar elementos (posiblemente muestre un error)
planetas.remove('La Tierra')
print(planetas)

# Eliminar elementos sin que se muestre ningún error en el caso de que no lo encuentre
planetas.discard('Jupiters')
print(planetas)

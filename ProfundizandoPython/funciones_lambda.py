# Funciones lambda
# Son funciones anónimas, sin nombre asignado, y son pequeñas (una línea de código)

# No es posible asignar una función a una variable
# mi_funcion = def sumar(a, b):  return a + b

# Con una función lambda (en una línea, sin paréntesis y sin return):
mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4,6)

print(f'Resultado de la suma: {resultado}')

# Función lambda que no recibe argumentos (debemos regresar una expresión válida)
mi_funcion_lambda = lambda : 'Función sin argumentos'
print(f'Llamar funcón lambda sin argumentos: {mi_funcion_lambda()}')

# Función lambda con parámetros por defecto:
mi_funcion_lambda = lambda a=2, b=3: a + b

# Podemos pasarle valores, o no, en cualquier caso funcionará y tendremos nuestra respuesta
resultado = mi_funcion_lambda()

print(f'Resultado de la suma: {resultado}')

# Función lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

# Funciones lambda con un poco de todo
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,4, 5,6,7,e=5,f=7)}')
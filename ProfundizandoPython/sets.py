# Profundizando en set
# Un set es una colección de elementos únicos y es mutable
# Los elementos de un set deben ser inmutables
conjunto = {'Juan', True, 18.0}
print(conjunto)

# Set vacío incorrecto (ES UN DICCIONARIO)
conjunto = {}

# Set vacío correcto:
conjunto = set()
print(conjunto)
print(type(conjunto))

# Mutable y con valores únicos
conjunto.add('Juan')
print(conjunto)

# Crear un set a partir de un iterable (si le damos valores duplicados borrará uno de los dos)
conjunto = set([4,5,7,8,4])
print(conjunto)

# Podemos agregar más elementos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar de un set a otro set (copia poco profunda, solo referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)

# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es igual en referencia? {conjunto is conjunto_copia}')

# Operaciones de conjuntos con set
# Persona con distintas características
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}

# Todos los ojos cafe y pelo rubio (Unión) (no se deben repetir elementos)
print(ojos_cafe.union(pelo_rubio))

# Invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))

# Solo recupera las personas con ojos cafe y pelo rubio (Intersección) (también puede ser conmutativa)
print(ojos_cafe.intersection(pelo_rubio))

# Pelo negro sin ojos café (Diferencia) (No conmutativa)
print(pelo_negro.difference(ojos_cafe))

# Todos las coincidencias: pelo negro u ojos café, pero NO ambos (Diferencia simétrica)
print(pelo_negro.symmetric_difference(ojos_cafe))


# Preguntar si un set está contenido dentro de otro (subset)
# revisamos si los elementos del primer set están contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# revisar si los elementos del primer set están contenidos en el segundo set
print(pelo_negro.issubset(menores_30))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoin)
print(pelo_negro.isdisjoint(pelo_rubio))
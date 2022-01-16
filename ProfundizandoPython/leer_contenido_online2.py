# Leer contenido online
from urllib.request import urlopen

palabras = []
with urlopen('http://antonioweb.es/projects/python/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')


# Contar ocurrencias de una cadena
print('Número de repeticones de "Universidad": ', contenido.count('Universidad'))

# Upper convierte a mayúsculas un str
print(contenido.upper())
print(contenido)

# Loer convierte a minúsculas un str
print(contenido.lower())
print(contenido)

# Python. Búsqueda abreviada de la cadena Python
print('Existe python?: ', 'python'.lower() in contenido.lower())
print('Existe PYTHON?: ', 'Python'.upper() in contenido.upper())

# startswith - inicia con
print('Inicia con "GlobalMentoring.com.mx": ', contenido.startswith('En GlobalMentoring.com.mx'))

# endswith - termina con
print('Termina con "GlobalMentoring.com.mx": ', contenido.lower().endswith('globalmentoring.com.mx'.lower()))

mensaje = 'Hola Mundo'
print(mensaje.lower().islower())

mensaje = 'HOLA MUNDO'
print(mensaje.isupper())

# Alinear cadenas
titulo = 'Sitio Web de GlobalMentoring.com.mx'
# print(titulo.center(50,'*'))
print(titulo.center(len(titulo)+10, '-'))

# Justificar a izquierda o derecha
print(titulo.ljust(len(titulo)+10, '*'))
print(titulo.rjust(len(titulo)+10, '*'))

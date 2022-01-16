# Profundizanddo en el tipo str 2:
from urllib.request import urlopen

# Multiplicación str
resultado = 3*' Hola'
print(f'Resultado: {resultado}')

# Multiplicación de tuplas:
resultado = 5*('Hola',5)
print(f'Resultado: {resultado}')

# Multiplicación de listas, útil para la inicialización de las mismas:
resultado = 10*[0]
print(f'Resultado: {resultado}, longitud: {len(resultado)}')

# Carácteres de escape
resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

# Caracter \b
resultado = 'Se va a elminar el punto suspensivo...\b\b\b'
print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\nuevo\juan'
print(f'Resultado: {resultado}')

# Raw string: no tiene en cuenta los caracteres de escape
resultado = r'Cadena con \n salto de línea'
print(f'Resultado: {resultado}')

# Reemplazar contenido en un str
with urlopen('http://antonioweb.es/projects/python/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')
print(contenido.replace(' ', '-'))

# Eliminar caracteres al inicio y al final de un str - strip
titulo = ' *** GlobalMentoring.com.mx *** '
print('Cadena original: ', titulo, len(titulo))
titulo = titulo.strip()
print('Cadena modificada: ', titulo, len(titulo))

titulo = '***GlobalMentoring.com.mx***'.strip('*') #Se puede elegir el lado, utilizando lstrip o rstrip
print('Cadena modificada 2:',titulo)


from urllib.request import urlopen

# Abrir URL.
r = urlopen("https://www.recursospython.com")
# Leer el contenido y e imprimir su tamaño.
print(len(r.read()))
# Cerrar para liberar recursos.
r.close()
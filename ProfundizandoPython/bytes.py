# Caracteres en bytes
caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

# Si se añade una 'b' antes de la cadena la convertimos a byte
mensaje = b'Universidad Python'
print(mensaje[0])
# Y podremos obtener el valor en Byte correspondiente
print(chr(mensaje[0]))

# El siguiente caracter en byte es:
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

# Convertir str a bytes
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado:', bytes)

# Convertir bytes a str
string2 = bytes.decode('UTF-8')
print('string decodificado:', string2)
print(string == string2)
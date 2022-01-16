# Abrimos el archivo en modo lectura: (la ruta debe ir con dos \\ para escapar este caracter en Windows)
# archivo = open('C:\\Users\\Antonio\\Documents\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r')
archivo = open('C:\\Users\\Antonio\\Documents\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r')
# Lectura completa del archivo:
# print(archivo.read())


# Leer algunos caracteres o líneas:
# print(archivo.readline())
# print(archivo.read(2))


# Si lo colocamos en un bucle..
'''for i in archivo.read():
    print(i)'''


# Para leer por líneas
# for linea in archivo:
#    print(linea)

# Leer líneas. Devuelve una lista, cada elemento es lo que hay en cada línea:
# print(archivo.readlines())
# print(archivo.readlines()[0])

# Abrimos un nuevo archivo y creamos una copia del anterior
# a - anexar información
archivo2 = open('C:\\Users\\Antonio\\Documents\\Cursos\\Python\\Archivos\\Leccion01\\copia.txt', 'a')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
from ManejoArchivos import ManejoArchivos

# Con with se abre y cierra el archivo automáticamente. Y si además, lo hacemos a través de una clase con los métodos enter y exit es perfecto
# with open('prueba.txt', 'r') as archivo:
#  print(archivo.read())


with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
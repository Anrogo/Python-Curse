# Definimos variable global
contador = 0

def mostrar_contador():
    print(contador)

def modificar_contador(c):
    global contador
    contador = c

modificar_contador(2)
mostrar_contador()
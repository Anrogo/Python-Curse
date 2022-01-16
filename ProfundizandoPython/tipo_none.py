# None significa "ausencia de valor"
variable = None

if bool(variable):
    print('Se considera verdadera')
else:
    print('Se considera false')

'''
8 formas de generar un bool False en Python
    1. Comilla simple o doble ''/"" (cadena vacía)
    2. Lista vacía []
    3. Tupla vacía ()
    4. Diccionario vacío {}
    5. Entero 0
    6. Flotante 0.0
    7. bool False
    8. None (a pesar de ser 'none type')
'''
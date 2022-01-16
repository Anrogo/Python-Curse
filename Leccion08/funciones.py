def miFuncion(nombre,apellido):
    print("Saludos desde mi función")
    print(f'Nombre {nombre}, Apellido: {apellido}')


# miFuncion('Antonio','Rodríguez')
# miFuncion('Karla','Lara')

def sumar(a = 0, b = 0):
    return a + b

# print(f'Resultado de la suma: {sumar()}')
# print(f'Resultado de la suma: {sumar(10,3)}')

# print(f'Resultado de la suma: {sumar(2,4)}')

# La función tendrá un parámetro de longitud variable, es decir se convierte en una tupla, y dentro leeremos sus valores:
def listarNombres(*nombres): # Por defecto se le llama *args pero no es obligatorio
    for nombre in nombres:
        print(nombre)

# listarNombres('Juan', 'Karla', 'María', 'Ernesto')
# listarNombres('Laura', 'Carlos')


# Función a la que se le pasa un diccionario (key-value) de forma variable:
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

# listarTerminos(IDE = 'Integrated Development Environment', PK = 'Primary Key')
# listarTerminos(DBMS = 'Database Management System')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
# Hay diferentes opciones: 
desplegarNombres('Carlos')
desplegarNombres((10,11))
desplegarNombres([1,2,3])
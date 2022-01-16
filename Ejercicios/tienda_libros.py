# Creamos una ficha con los datos de un libro de la tienda:
print('Proporciona los siguientes datos del libro:')
nombre = input('Proporciona el nombre del libro: ')
id = int(input('Proporciona el id del libro: '))
precio = float(input('Proporciona el precio del libro: '))
envioGratuito = input('Indica si el envío es gratuito o no (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, ddebe escribir True/False'

print(f'''
    Nombre: {nombre}
    Id: {id}
    Precio: {precio}
    Envío Gratuito?: {envioGratuito}
''')
# Profundizando en el tipo str
import math
from mi_clase import MiClase

# Concatenación automática en python:
'''variable = 'Adios'
mensaje = 'Hola ' 'Mundo. ' + variable
mensaje += ' Universidad' ' Python'
print(mensaje)
'''
# Para obtener información detallada sobre la clase str (o cualquier otra clase que queramos):
# help(str)
# help(math)
# help(str.center)
# help(MiClase)
# Para obtener la documentación de nuestro método, ya sea completa o paso a paso, sería de la siguiente manera:
'''print(MiClase.__doc__)
print(MiClase.__init__.__doc__)
print(MiClase.mi_metodo.__doc__)
print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))'''

'''mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje1 {mensaje1}, id{hex(id(mensaje1))}')
print(f'mensaje2 {mensaje2}, id{hex(id(mensaje2))}')
mensaje1 += 'adios'
print(f'mensaje1 {mensaje1}, id{hex(id(mensaje1))}')'''

'''# Podemos insertar valores dentro de una cadena con una tupla:
persona = ('Karla','Gomez',5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%(persona)
print(mensaje_con_formato)

# Y es exactamente lo mismo que hacer:
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
print(mensaje_con_formato%persona)'''

# Dar formato a un str. %s str, %d int, %f/%.2f float. Y además usando {} con o sin índices
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {0} Sueldo {2:.2f} Edad {1}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Sueldo {s:.2f} Nombre {n} Edad {e}'.format(n=nombre, e=edad, s=sueldo)
print(mensaje)

diccionario = {'nombre':'Ivan', 'edad':35, 'sueldo':8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)

# La mejor opción es f-string:
mensaje = f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

# Un truco final:
print(nombre, edad, sueldo, sep=', ')
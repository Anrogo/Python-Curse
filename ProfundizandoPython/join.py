# Método join:
#help(str.join)

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = '.'.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
print(f'Lista de cursos: {mensaje}')

diccionario = {'nombre':'Juan', 'apellido':'Perez','edad':'21'}
llaves = '-'.join(diccionario.keys())
valores = ' '.join(diccionario.values())
print(f'Llaves del diccionario: {llaves}, type:{type(llaves)}')
print(f'Valores del diccionario: {valores}, type:{type(valores)}')


print('-'.join(['02','septiembre','2021']))
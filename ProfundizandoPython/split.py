# Método split

# help(str.split)
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
print(f'Lista de cursos: {lista_cursos}')
print(f'Número de cursos: {len(lista_cursos)}')

lista_cursos = cursos_separados_coma.split(', ',3)
print(f'Lista de cursos: {lista_cursos}')
print(f'Número de cursos: {len(lista_cursos)}')
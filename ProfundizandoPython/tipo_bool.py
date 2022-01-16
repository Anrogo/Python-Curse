# bool contiene los valores de True y False
# Tipos numéricos, False para 0 y True todos los demás

valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

if '': # Es como escribir bool(''), y asi con cualquier valor que pongamos en un if
    print('Regresó verdadero')
else:
    print('Regresó falso')

if bool('1'):
    print('Regresó verdadero')
else:
    print('Regresó falso')
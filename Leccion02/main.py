# Otra manera de imprimir un resultado:
a = 3
b = 2
suma = a + b
# print('Resultado suma:',a,"+", b, "=", suma)
print(f'Resultado suma: {suma}')
# Se puede dividir de dos maneras, con decimales o de forma entera:
division = a / b
print(f'Resultado division normal: {division}')
division2 = a // b
print(f'Resultado division entera: {division2}')

# Y para multiplicar con exponentes sería de forma similar:
exponente = b ** a
print(f'Resultado exponente: {exponente}')

# Aumentar/reducir un contador
cont = 1
cont += 1
print(cont)

# Número par e impar
'''
n = int(input("Escribe un valor numérico: "))

if n % 2 == 0:
    print(f'El valor de a {n} es número par')
else:
    print(f'El valor de a {n} es número impar')
'''

# Conversión de valores 
numero = int(input('Proporciona un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Número proporcionado: {numero} - {numeroTexto}')
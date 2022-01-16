# Desempaquetar
# Para desempaquetar una lista se puede utilizar *
numeros = [1,2,3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# Para diccionarios se utiliza el **

# Y si lo que queremos es pasarle los valores a una función también se puede aplicar el unpacking con *
def sumar(a, b, c):
    print(f'Suma: {a+b+c}')

sumar(*numeros)

# Extraer algunas partes de una lista
mi_lista = [1,2,3,4,5,6]
a, *b, c, d = mi_lista
print(a,b,c,d)


# Unir listas desempaquetando 2 listas en el interior de otra. Quedaría como una única lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [*lista1,*lista2]
print(f'Lista de listas: {lista3}')

# Unir diccionarios (de la misma manera pero usando **)
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir diccionarios: {dic3}')

# Construir un alista a partir de un str = str.split(caracter a caracter)
lista = [*'HolaMundo']
print(lista)
print(*lista, sep='')
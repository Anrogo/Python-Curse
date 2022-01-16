# Primero tenemos una tupla:
tupla = (13, 1 , 8, 3, 2, 5, 8)
print(tupla)

# Iteramos con la condición de que sea menor que 5 para pertenecer a nuestra nueva lista
lista = []

for n in tupla:
    if n < 5:
        lista.append(n)

# Mostramos como queda la lista
print(lista)
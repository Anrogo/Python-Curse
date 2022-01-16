# Imprime de manera descendente y recursiva desde el número que le indiquemos hasta 1
def descendente(numero):
    if numero >= 1:
        print(numero)
        descendente(numero-1)

descendente(5)
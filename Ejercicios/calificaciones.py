# El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

nota = int(input("Introduce un valor numérico (0-10): "))

if 0 <= nota <6:
    print('F')
elif 6 <= nota <7:
    print('D')
elif 7 <= nota <8:
    print('C')
elif 8 <= nota <9:
    print('B')
elif 9 <= nota <=10:
    print('A')
else:
    print('Valor desconocido')


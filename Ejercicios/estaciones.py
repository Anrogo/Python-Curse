# Calcular la estación del año según el mes introducido:
mes = int(input('Proporciona mes del año (1-12): '))
estacion = None

if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Invierno'

elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'

elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'

elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'

else:
    estacion = 'No exite el mes'

print(f'Para el mes de {mes} la estación es: {estacion}')
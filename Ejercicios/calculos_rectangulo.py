# Calcular el área y el perímetro de un rectángulo. Los datos son proporcionados por el usuario:
alto = float(input("Proporciona el alto: "))
ancho = float(input("Proporciona el ancho: "))
print(f'Área: {round(alto*ancho,2)}')
print(f'Perímetro: {round((alto+ancho)*2,2)}')
# Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

# Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit: celsius * 9/5 + 32 

def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius: (fahrenheit-32) * 5/9

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit-32) * 5/9

# Realizamos algunas pruebas de conversión
celsius = float(input('Proporcione su valor en celsius: '))
resultado = celsius_fahrenheit(celsius)
# Los dos puntos después de la variable de resultado dan un formato de 2 digitos flotantes
print(f'{celsius} ºC a ºF: {resultado:.2f}')
fahrenheit = float(input('Proporcione su valor en fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} ºF a ºC: {resultado:.2f}')
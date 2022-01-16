from NumerosIdenticosException import NumerosIdenticosException
resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        # Para lanzar una excepción personalizada:
        raise NumerosIdenticosException('Los números son idénticos')
    resultado = a / b

except ZeroDivisionError as zde:
    print(f'ZeroDivisionError -> Ocurrió el siguiente error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'TypeError -> Ocurrió el siguiente error: {te}, {type(te)}')
except Exception as e:
    print(f'Exception -> Ocurrió el siguiente error: {e}, {type(e)}')
else: 
    # Se ejecuta siempre que no se lanza ningúna excepción:
    print('No se arrojó ninguna excepción')
finally: 
    # Siempre se ejecutará al final, pase lo que pase
    print(f'Ejecución del bloque finally')

print(f'Resultado: {resultado}')
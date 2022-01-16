# Manejo de valores infinitos
import math
from decimal import Decimal

# Representación del número positivo infinito:
infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}')

infinito_positivo = float('2.0')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}')

# Representación del número negativo infinito:
infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'¿Es infinito?: {math.isinf(infinito_negativo)}')

# Otra manera de asignar el valor de infinito positivo:
infinito_positivo = math.inf
infinito_negativo = -math.inf
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}')

# Ahora utilizamos el módulo Decimal:
infinito_positivo = Decimal('Infinity')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}')
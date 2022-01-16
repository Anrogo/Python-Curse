import math
from decimal import Decimal
# NaN - Not a number (no es un número)
# NaN no es sensible a mayús/minús
# NaN es un tipo de dato numérico indefinido
a = float('NaN')
a = Decimal('nan')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')
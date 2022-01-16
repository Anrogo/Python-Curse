# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# La función debe regresar el total del pago incluyendo el porcentaje de impuesto proporcionado.
# Ej. Si llamamos a la función calcular_total(1000, 16) debe retornar el valor 1,160.0
# Los valores los debe proporcionar el usuario y se procesados con la función input, convirtiendolos a tipo float.
def calcular_total(precio, imp):
    if imp > 1:
        imp = imp/100
    return precio * (1 + imp)

dinero = float(input('¿Cuál es el precio sin impuestos? '))
impuesto = float(input('Impuesto: '))
print(f'Precio (IVA incluido: {impuesto} %) {calcular_total(dinero, impuesto)}')
from Empleado import Empleado
from Gerente import Gerente

def imprimir_detalles(objeto):
    #print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente): # solo si el objeto pertenece a la clase Gerente
        print(objeto.departamento) # Pdremos mostrar su atributo de departamento

empleado1 = Empleado('Juan', 5000)
imprimir_detalles(empleado1)
gerente = Gerente('Juan', 5000, 'Marketing')
imprimir_detalles(gerente)

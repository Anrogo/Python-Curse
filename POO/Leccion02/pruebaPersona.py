from Persona import Persona

print('Creación objetos'.center(30,'-'))

persona1 = Persona('Juan', 'Perez', 28)
persona2 = Persona('Karla', 'Gomez', 31)

persona1.mostrarDetalle()
persona2.mostrarDetalle()

print('Eliminación objetos'.center(30,'-'))
del persona1
del persona2
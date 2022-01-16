class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos): #no tiene que llamarse SELF de manera obligatoria, pero sí ser el primer argumento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrarDetalle(self): #debe contener como mínimo el argumento self
        print(f'Objeto Persona {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

# Como atributos a la clase se pueden añadir de manera opcional, primero, una tupla y, en segundo caso, un diccionario
persona1 = Persona('Juan', 'Perez', 28, '44553322', 2, 3, 5, m='manzana', p='pera')
persona1.mostrarDetalle()
persona1.telefono = '55441122'

persona2 = Persona('Karla', 'Gomez', 31)
persona2.mostrarDetalle()


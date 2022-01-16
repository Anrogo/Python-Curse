# Ejemplo de sobrecarga de operadores con la clase Persona
class Persona:
    def __init__(self, nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro): # Suma
        return f'{self.nombre} {otro.nombre}'

    def __sub__(self, otro): # Resta
        return self.edad - otro.edad   

persona1 = Persona('Juan', 27)
persona2 = Persona('Carlos', 23)
print(persona1 + persona2)
print(persona1 - persona2)
# obj1 + obj2
# obj1.__add__(obj2)
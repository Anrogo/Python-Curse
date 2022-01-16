class Persona:
    # Variable de clase:
    contador_personas = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    def __str__(self) -> str:
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


# Pruebas:
persona1 = Persona('Juan', 28)
persona2 = Persona('Karla',23)
persona3 = Persona('Eduardo',33)
print(persona1)
print(persona2)
print(persona3)
persona4 = Persona('María',35)
print(persona4)
print(f'Valor contador de personas: {Persona.contador_personas}')
from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    edad: int
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0
    
    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')
        if not self.apellido:
            raise ValueError(f'Valor apellido vacío: {self.apellido}')

domicilio1 = Domicilio('Calle Malaga',3)
persona1 = Persona('Juan','Lopez',23,domicilio1)
print(f'{persona1!r}')

# Variable de clase:
print(f'Variable clase: {Persona.contador_personas}')

# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')

# Variable con valores vacíos (daría error)
# persona_vacia = Persona('Antonio','Rodriguez',1)
# print(persona_vacia)

# Revisar igualdad entre objetos. El dataclass tiene eq=true por defecto en su implementación
persona2 = Persona('Susana','Martin',20, Domicilio('Calle Malaga',3))

print(f'Objetos iguales?: {persona1.domicilio == persona2.domicilio}')

# Agregar esta clase a una colección
coleccion = {persona1, persona2}
print(coleccion)
# Frozen = True
# coleccion[0].nombre = 'Juan Carlos'
# persona1.nombre = 'Juan Carlos'
class Persona:
    def __init__(self, nombre, apellido, edad): #no tiene que llamarse SELF de manera obligatoria, pero sí ser el primer argumento
        self._nombre = nombre # Este sería un atributo encapsulado de forma privada (_) y con __ sería protected y es inaccesible de cualquier forma
        self._apellido = apellido
        self._edad = edad

    # Método GET de nombre
    @property
    def nombre(self):
        return self._nombre

    # Método SET de nombre. Si no le hacemos método set y es privado sería "read-only"
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self): #debe contener como mínimo el argumento self
        print(f'Objeto Persona {self._nombre} {self._apellido} {self._edad}')

    # Destructor de objetos:
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

# Solo ejecutaremos el código de prueba cuando se ejecute el propio archivo:
if __name__ == '__main__':

    # Como atributos a la clase se pueden añadir de manera opcional, primero, una tupla y, en segundo caso, un diccionario
    persona1 = Persona('Juan', 'Perez', 28)

    # Acceso al atributo desde su get:
    print(persona1.nombre)
    print(persona1.apellido)
    print(persona1.edad)

    # Modificación mediante el set de nombre:
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.mostrarDetalle()

    # Ahora se va a mostrar el nombre del archivo
    print(__name__)

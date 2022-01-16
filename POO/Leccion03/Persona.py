class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self): 
        print(f'Objeto Persona {self._nombre} {self._edad}')

    #Este método mostrará la info al intentar "printar" el objeto
    def __str__(self) -> str:
        return f'Persona [Nombre: {self._nombre}, Edad: {self._edad}]' 

    # Destructor de objetos:
    # def __del__(self):
    #    print(f'Persona: {self._nombre}')

# Clase hija que hereda de Persona:
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def __str__(self) -> str:
        return f'Empleado [Sueldo: {self._sueldo}] {super().__str__()}' 

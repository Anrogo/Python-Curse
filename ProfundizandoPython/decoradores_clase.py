import inspect
# Decoradores de Clae
# Permiten transformar de manera prográmatica nuestra clase
# Es similar a los decoradores de funciones (es metaprogramación)

def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')


    # Recuperamos los atributos de la clase con el método vars
    atributos = vars(cls)
    # Iteramos cada atributo
    #for nombre, atributo in atributos.items():
    #    print(nombre, atributo)

    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros de init, excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

    # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # Property es un valor d etipo built-in para preguntar si
        # se está utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro para el parámetro: {parametro}')

    # Crear el método repr dinámicamente
    def metodo_repr(self):
        # Obtenemos el nombre de la clase dinámicamente
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')

        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresión generadora, crear nombre_atr = valor_atr. El '!r' añadirá comillas simples al valor del atributo
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Creamos la lista del generador
        lista_arg = list(generador_arg)
        # Imprimimos la lista
        print(f'Lista del generador: {lista_arg}')

        # Creamos la cadena a partir de la lista de argumentos
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')

        # Creamos la forma del método __repr__, sin su nombre,
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'

        return f'-------------- {resultado_metodo_repr} --------------'
    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls, '__repr__', metodo_repr)

    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido,edad):
        print('--------------Se ejecuta el inicializador--------------')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    #def __repr__(self):
    #    return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

persona1 = Persona('Juan', 'Perez',17)
print(persona1)
persona2 = Persona('Antonio', 'Sanchez',28)
print(persona2)
persona3 = Persona('Kika', 'Lopez',25)
print(persona3)

# Tiene los métodos de propiedad nombre, apellido, repr
# print(dir(Persona))

# Para ver si tiene el método repr sobreescrito. Mostrará el método que hemos escrito antes..
# codigo_repr = inspect.getsource(persona1.__repr__)
# print(codigo_repr)
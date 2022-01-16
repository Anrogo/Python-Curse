class MiClase:

    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        # Permite acceder directamente a la variable de clase:
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

# Podremos acceder directamente a la "constante"
# print(MiClase.variable_clase)

# Y crearlas en el momento:
MiClase.variable_clase2 = 'Valor varible clase 2'
# print(MiClase.variable_clase2)

# Pero los atributos solo son accesibles al instanciar la clase en un nuevo objeto
miClase = MiClase('Valor variable instancia')
# print(miClase.variable_instancia)

# MiClase.metodo_clase()
miObjeto1 = MiClase('variable_instancia')
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()

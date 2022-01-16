from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erróneo ancho: {ancho}')
            self._ancho = 0
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erróneo alto: {alto}')
            self._alto = 0

    @property    
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erróneo ancho: {ancho}')

    @property    
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erróneo alto: {alto}')

    # Para crear nuestra clase abstracta es necesario importar el ABC = Abstract Base Class
    @abstractmethod
    def calcularArea(self):
        pass # No tiene ninguna implementación

    def __str__(self) -> str:
        return f'Figura Geometrica [Ancho: {self._ancho}, Alto: {self._alto}]'

    # Método invisible fuera de la clase, que permite validar sus valores:
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

    
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton


class Computadora:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self) -> str:
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        '''
if __name__ == '__main__':

    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('Logitech', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HP 15', monitor1, teclado1, raton1)
    teclado2 = Teclado('Acer', 'Bluetooth')
    raton2 = Raton('Razer', 'Bluetooth')
    monitor2 = Monitor('Acer', 19)
    computadora2 = Computadora('ACER Gaming', monitor2, teclado2, raton2)
    print(computadora1)
    print(computadora2)
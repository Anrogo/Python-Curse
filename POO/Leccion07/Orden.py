from Producto import Producto


class Orden: # Se refiere a "Pedido"
    contador_ordenes = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_orden = Orden._generar_siguiente_valor()
        self._productos = list(productos)

    @property
    def productos(self):
        return self._productos

    def agregar_productos(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self) -> str:
        productos_str = ''
        for producto in self.productos:
            productos_str += producto.__str__() + ''
        return f'\nOrden: {self._id_orden},\nProductos:\n{productos_str}'


if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos = [producto1, producto2]
    orden1 = Orden(productos)
    print(orden1)
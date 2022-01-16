class Producto:

    contador_productos = 0

    @classmethod
    def _generar_siguiente_valor(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio) -> None:
        self._id_producto = Producto._generar_siguiente_valor()
        self._nombre = nombre
        self._precio = precio
    
    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    def __str__(self) -> str:
        return f'Id Producto: {self.id_producto}, Nombre: {self.nombre}, Precio: {self.precio}\n'

    
if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalón', 150.00)
    print(producto2)
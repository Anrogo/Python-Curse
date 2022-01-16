class NumerosIdenticosException(Exception):

    def __init__(self, mensaje, *args: object) -> None:
        super().__init__(*args)
        self.message = mensaje
        
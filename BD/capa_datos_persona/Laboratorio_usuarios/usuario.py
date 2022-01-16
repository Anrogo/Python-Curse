from logger_base import log

class Usuario:

    def __init__(self, id_usuario=None, username=None, password=None):
        self._id_usuario = id_usuario
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return f'''[ID: {self._id_usuario}] Username: {self._username} -> Password: {self._password}'''

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_persona):
        self._id_usuario = id_persona

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

if __name__ == '__main__':
    usuario1 = Usuario(1, 'Juanito', '12345')
    log.debug(usuario1)
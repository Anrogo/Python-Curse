from usuario import Usuario
from logger_base import log
from cursor_del_pool import CursorDelPool

class UsuarioDAO:
    '''
        DAO (Data Access Object)
        CRUD (Create Read Update Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):

        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()

            usuarios = []

            for registro in registros:
                persona = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(persona)

            return usuarios

    @classmethod
    def insertar(cls, usuario):

        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario insertado: {usuario}')

            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):

        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario._id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')

            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valor = (usuario.id_usuario,)
            cursor.execute(cls._ELIMINAR, valor)
            log.debug(f'Usuarios eliminados: {usuario}')

            return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    usuario1 = Usuario(username='prueba', password='123')
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuarios insertados: {usuarios_insertados}')

    # Actualizar registro
    usuario1 = Usuario(username='prueba', password='1234')
    usuarios_actualizados = UsuarioDAO.actualizar(usuario1)
    log.debug(f'Usuarios actualizados: {usuarios_actualizados}')

    # Seleccionar registros
    personas = UsuarioDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

    # Eliminar un registro
    persona2 = Usuario(id_usuario = 5)
    UsuarioDAO.eliminar(persona2)
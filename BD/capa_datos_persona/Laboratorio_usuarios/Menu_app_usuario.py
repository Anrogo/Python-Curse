from usuario import Usuario
from usuario_dao import UsuarioDAO
from logger_base import log

def menu():
    print('''Opciones:
                1. Listar usuarios
                2. Agregar usuario
                3. Modificar usuario
                4. Eliminar usuario
                5. Salir
    ''')

def opciones(n):
    if n == 1:
        listar_usuarios()
    elif n == 2:
        agregar_usuario()
    elif n == 3:
        modificar_usuario()
    elif n == 4:
        eliminar_usuario()
    elif n == 5:
        log.info('Adiós y gracias por su visita')
    else:
        log.error('Opción inválida. Vuelve a intentarlo..')

def listar_usuarios():
    # Seleccionar registros
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.info(usuario)

def agregar_usuario():
    # Insertar un nuevo registro
    username_var = input('Escribe el username: ')
    password_var = input('Escribe el password: ')
    usuario = Usuario(username=username_var, password=password_var)
    usuarios_insertados = UsuarioDAO.insertar(usuario)
    #log.info(f'Usuarios insertados: {usuarios_insertados}')

def modificar_usuario():
    # Actualizar registro
    id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
    username_var = input('Escribe el username: ')
    password_var = input('Escribe el password: ')
    usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
    usuarios_actualizados = UsuarioDAO.actualizar(usuario)
    #log.info(f'Usuarios actualizados: {usuarios_actualizados}')

def eliminar_usuario():
    # Eliminar un registro
    id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
    usuario = Usuario(id_usuario=id_usuario_var)
    usuarios_eliminados = UsuarioDAO.eliminar(usuario)
    #log.info(f'Usuarios eliminados: {usuarios_eliminados}')


def recibir_opcion():
    try:
        n = int(input('Escribe tu opción (1-5): '))
        return n
    except Exception as e:
        log.error(f'Excepción encontrada: {e}')

def app():

    # Menu en bucle infinito
    opcion = None

    while opcion != 5:
        menu()
        # Nos aseguramos de recibir la opción como número entero y no una cadena o cualquier caracter introducido por error..
        opcion = recibir_opcion()
        if opcion != 5: # Si no se selecciona SALIR (5) comprobaremos qué quiere el usuario:
            opciones(opcion)

    else:
        log.info('Salimos de la aplicación...')

# Aplicación para gestionar una lista de usuarios CRUD:
app()


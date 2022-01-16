import logging as log

# Marca el nivel mínimo que se mostrará de mensajes del log (en nivel Debug se mostrarán todos porque es el más bajo):
# Además se puede configurar un handler, o manejador, para tener nuestro archivo log con mensajes personalizados
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('lista-usuarios.log'),
                    log.StreamHandler()
                ])

# Los ejemplos de mensaje:
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel crítico')
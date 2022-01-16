import psycopg2

# Se introducen los parámetros de conexión a bbdd
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    with conexion:

        # Se crea y ejecuta la sentencia mediante 'cursor'
        with conexion.cursor() as cursor:

            # Para eliminar varios registros a la vez (CUIDADO CON EL WHERE):
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'

            # Se piden los ID separados por ,
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')

            # Y se juntan en una tupla de tuplas generada mediante un split
            valores = (tuple(entrada.split(',')),)

            # Finalmente ejecutamos el borrado:
            cursor.execute(sentencia, valores)

            # Ahora es necesario guardar los cambios en la base de datos, sin embargo con WITH se hace automático
            # conexion.commit()

            # Para comprobar que los cambios se han realizado correctamente:
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()

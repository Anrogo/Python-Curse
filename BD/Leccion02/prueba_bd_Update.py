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
            sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'

            # La tupla de valores con la que se sustituye en la sentencia SQL:
            valores = (('Juan', 'Perez', 'jperez@mail.com', 1),
            ('Esther', 'Sanchez', 'esanchez@mail.com', 4),)

            # Para actualizar un registro:
            cursor.executemany(sentencia, valores)

            # Ahora es necesario guardar los cambios en la base de datos, sin embargo con WITH se hace automático
            # conexion.commit()

            # Para comprobar que los cambios se han realizado correctamente:
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()

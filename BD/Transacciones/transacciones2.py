import psycopg2 as bd

# Se introducen los parámetros de conexión a bbdd
conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'

            valores = ('Alex', 'Rojas', 'arojas@mail.com')

            cursor.execute(sentencia, valores)

            # Ahora hacemos una segunda operación:
            sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'

            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)

            cursor.execute(sentencia, valores)

except Exception as e:
    # Si falla cualquiera de las operaciones de la transacción llegaremos aquí:
    print(f'Ocurrió un error, se hizo rollback de la transacción: {e}')

finally:
    print('Terminó la transacción')
    conexion.close()

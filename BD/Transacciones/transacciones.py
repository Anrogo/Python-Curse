import psycopg2 as bd

# Se introducen los parámetros de conexión a bbdd
conexion = bd.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')

try:
    # Se inicia la transacción
    # Desactivamos el auto commit para verificar que se realiza de manera correcta
    conexion.autocommit = False

    cursor = conexion.cursor()

    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'

    valores = ('Carlos', 'Lara', 'clara@mail.com')

    cursor.execute(sentencia, valores)

    # Ahora hacemos una segunda operación:
    sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'

    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)

    cursor.execute(sentencia, valores)

    # Finaliza la transacción
    # Confirmamos el commit manualmente
    conexion.commit()

    print('Terminó la transacción')

except Exception as e:
    # Si falla cualquiera de las operaciones de la transacción llegaremos aquí:
    conexion.rollback()
    print(f'Ocurrió un error, se hizo rollback de la transacción: {e}')

finally:
    conexion.close()

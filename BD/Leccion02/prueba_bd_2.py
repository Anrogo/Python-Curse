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
            sentencia = 'SELECT id_persona, nombre, email FROM persona WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_persona: ')
            cursor.execute(sentencia, (id_persona,))

            # Al hacer el filtrado por id solo nos interesa un registro de la tabla, y se utiliza fetchone:
            registro = cursor.fetchone()

            print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
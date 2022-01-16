import psycopg2

# Se introducen los parámetros de conexión a bbdd
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db')
print(conexion)
try:
    with conexion:

        # Se crea y ejecuta la sentencia mediante 'cursor'
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)

            # Se estructuran los registros en forma de tupla para poder acceder a ellos:
            registros = cursor.fetchall()

            for persona in registros:
                print(persona)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
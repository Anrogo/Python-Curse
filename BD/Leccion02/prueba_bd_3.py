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
            sentencia = 'SELECT id_persona, nombre, email FROM persona WHERE id_persona IN %s'
            # Es necesario pasar una tupla, así que hay que añadir la coma al final. Y si pedimos los datos
            # manualmente necesitamos convertir a tupla de tuplas llaves_primarias = ((1,2,4),)
            entrada = input('Proporciona los id\'s a buscar (separando por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, llaves_primarias)

            # Al hacer el filtrado por id solo nos interesa un registro de la tabla, y se utiliza fetchone:
            registros = cursor.fetchall()

            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()

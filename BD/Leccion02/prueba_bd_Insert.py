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
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valor = ('Carlos', 'Lara', 'clara@mail.com')
            valores = (
                ('Nati', 'Garrido', 'natiga@mail.com'),
                ('Angel', 'Quintana', 'aquintana@mail.com'),
                ('María', 'González', 'mgonzalez@mail.com'),
            )

            # Para insertar un registro se utiliza cursor con el método execute a secas para introducir la tupla:
            cursor.execute(sentencia, valor)

            # Y si queremos insertar varios se utiliza executemany y la tupla de tuplas:
            cursor.executemany(sentencia, valores)

            # Ahora es necesario guardar los cambios en la base de datos, sin embargo con WITH se hace automático
            # conexion.commit()

            # Para comprobar que los cambios se han realizado correctamente:
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()

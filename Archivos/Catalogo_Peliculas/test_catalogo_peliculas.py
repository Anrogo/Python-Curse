from Dominio.Pelicula import Pelicula
from Servicio.catalogo_peliculas import CatalogoPeliculas as cp


print('Catálogo de películas'.center(50,'-'))

opcion = None

while opcion != 4:
    print(f'''
Opciones:
1. Agregar película
2. Lister peliculas
3. Eliminar catálogo de películas
4. Salir''')
    try:
        opcion = int(input('Escribe tu opción (1-4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar_peliculas()

        elif opcion == 4:
            print('\nHasta la próxima! ;D')

        else:
            print('\nOpción inválida, vuelve a intentarlo por favor...')

    except Exception as e:
        print('\nSe ha encontrado un error ',e)
        opcion = None

else:
    print('\nSaliendo del programa...\n')
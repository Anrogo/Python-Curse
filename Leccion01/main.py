
a = "2"
b = "3"
c = 14.5
miVariable = int(a) + int(b)
print(miVariable)

# Para mostrar la dirección de memoria donde se almacena nuestra variable:
print(id(miVariable))
print(id(a))
print(id(b))
miVariable = "Saludos desde Python"
print(miVariable)

# Tipo de variable:
print(type(a))
print(type(miVariable))
print(type(False))
print(type(c))
# Existen dos maneras de mostrar cadenas por pantalla:
miGrupoFavorito = "Aeroesmith"
comentario = "The Best Rock Band"
print("Mi grupo favorito es: " + miGrupoFavorito + " " + comentario)
print("Mi grupo favorito es:", miGrupoFavorito, comentario)

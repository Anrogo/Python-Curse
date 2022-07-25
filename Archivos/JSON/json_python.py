# Leer archivo json
# JSON = JavaScript Object Notation

import json
from urllib.request import Request, urlopen
import urllib.request

# URL de consulta con el JSON

URL = Request('https://www.globalmentoring.com.mx/api/personas.json')

# Se agrega un header de lectura a la petición de la url

URL.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
# URL.add_header('User-Agent', 'Firefox/78.0')

# Se hace dicha conexión, mediante urlopen ya con el header añadido. Y se obtiene una respuesta

respuesta = urlopen(URL)

# print(respuesta)

# Se lee el cuerpo de la respuesta

cuerpo_respuesta = respuesta.read()

# print(cuerpo_respuesta)

# Procesamos la respuesta decodificandola con utf-8
# Opcion alternativa: cuerpo_respuesta.decode('utf-8')
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

# Imprimimos solo los nombres de las personas
# Para ello convetirmos el JSON a listas y diccionarios en python
for persona in json_respuesta['personas']:
    print(f'Persona: {persona["nombre"]} {persona["edad"]}')

# Accedemos a las variables independientes del JSON
print(f'Total de personas: {json_respuesta["total"]}')
print(f'Mensaje: {json_respuesta["mensaje"]}')
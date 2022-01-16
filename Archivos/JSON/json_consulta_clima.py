import json
import urllib.request
from urllib.request import Request, urlopen

URL = Request('https://globalmentoring.com.mx/api/clima.json')

URL.add_header('User-Agent', 'Firefox/78.0')

respuesta = urlopen(URL)

cuerpo_respuesta = respuesta.read()

json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))

# print(json_respuesta)

#for clima in json_respuesta["clima"]:
    #print(clima)

# Ejercicio 1. acceder a la descripción del clima
descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
# Es equivalente a: json_respuesta["clima"][0]['descripcion']
print(f'Descripción del clima: {descripcion_clima}')

# Ejercicio 2. Mostrar temperatura max y min
temp_min = json_respuesta['principal']['temp_min']
print(f'Temperatura minima: {temp_min}')
temp_max = json_respuesta['principal']['temp_max']
print(f'Temperatura maxima: {temp_max}')
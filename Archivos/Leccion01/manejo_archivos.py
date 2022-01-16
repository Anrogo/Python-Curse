try: 
    # Abrimos el archivo, si existe, en modo escritura (con la codificación de caracteres para poder interpretar las tildes)
    archivo = open('C:\\Users\\Antonio\\Documents\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adiós')
except Exception as e:
    print(f'Ha ocurrido un error: {e}')
finally:
    archivo.close()
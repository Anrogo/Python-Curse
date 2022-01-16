# Calcular la estación del año según el edad introducido:
edad = int(input('Proporciona tu edad: '))
etapa = None

if 0 <= edad < 10 :
    etapa = 'La infancia es increíble...'

elif 10 <= edad < 20 :
    etapa = 'Muchos cambios y mucho estudio...'

elif edad >= 20 and edad <=30 :
    etapa = 'Amor y comienza el trabajo...'

else:
    etapa = 'Etapa de vida NO reconocida'

print(f'Para tu edad, {edad}, estás en: {etapa}')
#https://docs.djangoproject.com/en/3.0/ref/models/fields/
#https://docs.djangoproject.com/en/3.0/howto/custom-model-fields/

#Antes de empezar la leccion borrar el archivo sqlite3 para ahora trabajar con postregresql 

#instalar postgresql:
python -m pip install psycopg2

#crea base de datos django_db en pgadmin, sin nada mas

#configurar postregresql en archivo settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

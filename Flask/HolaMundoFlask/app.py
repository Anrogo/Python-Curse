from flask import Flask, request, render_template, url_for, jsonify
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def inicio():
    # app.logger.debug('Mensaje de debug')
    app.logger.info(f'Entramos al path: {request.path}')
    return "<h1>Hola mundo!</h1>"

@app.route("/saludar/<nombre>")
def saludar(nombre):

    return  f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'Tienes {edad} años'

@app.route('/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre_llave=nombre)

@app.route('/redireccionar')
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Juan'))

@app.route('/salir')
def salir():
    return abort(404)

# Captura los errores que se produzcan y muestra la plantilla personalizada:
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


# REST Representational State Transfer
@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    # app.logger.debug('Mensaje de debug')
    app.logger.info(f'Entramos al path: {request.path}')
    return "<h1>Hola mundo!</h1>"

@app.route("/saludar/<nombre>")
def saludar(nombre):

    return  f'Saludos {nombre}'

@app.route('/edad/<int:edad>')
def edad(edad):
    return f'Tienes {edad} años'
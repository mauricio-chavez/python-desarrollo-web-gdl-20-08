from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/hola')
def hola():
    return '<h1>Hola mundo</h1>'

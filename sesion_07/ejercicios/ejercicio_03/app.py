from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world_flask():
    products = ['Pizza', 'Tacos', 'Lasagna']
    name = 'flask'.capitalize()
    return render_template('index.html', name=name, products=products)


@app.route('/<name>')
def hello_world(name):
    products = ['Pizza', 'Tacos', 'Lasagna']
    name = name.capitalize()
    return render_template('index.html', name=name, products=products)


@app.route('/suma/<int:n1>/<int:n2>')
def sumar(n1, n2):
    resultado = n1 + n2
    return render_template('suma.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    name = request.args.get('name')
    if not name:
        name = 'Flask'
    products = ['Pizza', 'Tacos', 'Lasagna']
    return render_template('index.html', name=name, products=products)

@app.route('/suma')
def sumar():
    n1 = request.args.get('n1') # None
    n2 = request.args.get('n2') # 10

    if n1 and n2:
        resultado = int(n1) + int(n2) # 20
    else:
        resultado = None
    return render_template('suma.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

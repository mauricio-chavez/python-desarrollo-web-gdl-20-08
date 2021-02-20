from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/suma')
def suma():
    n1 = request.args['n1'] # 10
    n2 = request.args['n2'] # 10
    resultado = int(n1) + int(n2) # 20
    return 'Resultado = {}'.format(resultado)


if __name__ == '__main__':
    app.run(debug=True)

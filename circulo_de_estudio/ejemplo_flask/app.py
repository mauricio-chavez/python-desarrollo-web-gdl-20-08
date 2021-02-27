from flask import Flask, request, render_template

app = Flask(__name__)

products = []


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form['name']
        products.append(name)
    return render_template("index.html", products=products)


if __name__ == '__main__':
    app.run(debug=True)

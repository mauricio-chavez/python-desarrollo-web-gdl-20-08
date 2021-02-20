from flask import Flask, render_template, request
from forms import ProductForm

app = Flask(__name__)
products = []


@app.route('/', methods=['GET', 'POST'])
def product_view():
    errors = []
    if request.method == 'POST':
        form = ProductForm(request.form)
        if form.validate():
            product = form.data
            products.append(product)
        else:
            for errors_list in form.errors.values():
                if type(errors_list) == list:
                    for error in errors_list:
                        errors.append(error)
    return render_template('products.html', products=products, errors=errors)


if __name__ == '__main__':
    app.run(debug=True)

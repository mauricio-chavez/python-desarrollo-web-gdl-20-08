import wtforms

class ProductForm(wtforms.Form):
    name = wtforms.StringField()
    amount = wtforms.FloatField()

    def validate_name(self, name):
        if not name.data:
            raise wtforms.ValidationError('El nombre es necesario')

    def validate_amount(self, amount):
        if not amount.data:
            raise wtforms.ValidationError('El monto es necesario')
        if amount.data <= 0:
            raise wtforms.ValidationError('El monto debe ser mayor a cero')

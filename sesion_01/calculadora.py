primero = input('Primer número: ')
segundo = input('Segundo número: ')
operacion = input('Operación (+, -, *, /): ')

# Se convierten a flotantes porque vienen como cadenas
primero = float(primero)
segundo = float(segundo)

if operacion == '+':
    resultado = primero + segundo
elif operacion == '-':
    resultado = primero - segundo
elif operacion == '*':
    resultado = primero * segundo
elif operacion == '/':
    if (segundo == 0):
        resultado = 'division_cero'
    else: 
        resultado = primero / segundo
else:
    resultado = 'error'


if (resultado == 'error'):
    print('Error: Operación no definida')
elif (resultado == 'division_cero'):
    print('Error: División entre cero')
else:
    print('El resultado es {}'.format(resultado))

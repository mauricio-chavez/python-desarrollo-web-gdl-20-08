"""
Reglas para nombrado de variables

* Una variable contiene letras, números y underscores "_"
* Las variables NO pueden empezar con un número a pesar de que se pueden usar en cualquier otra parte


RECOMENDACIONES:

* Usar snake case (separamos por underscore y todo en minúsculas) (LEGIBILIDAD)
* Usar nombres en inglés (CONSISTENCIA) (MANTENIBILIDAD)
"""

nombre_completo = 'Mauricio Chávez'


# Operadores de comparación

igual_que = 10 == 10
diferente_que = 10 != 10
mayor_que = 10 > 20
mayor_igual_que = 10 >= 7
menor_que = 10 < 20
menor_igual_que = 10 <= 7


# Condicionales

# age = 15

# if age >= 18:
#     print('Pasas al bar')
#     print('Diviértete')
# elif age >= 16:
#     print('Necesitamos un permiso de tus padres o tutores')
# else:
#     print('No puedes pasar 😡')

age = 18

if age >= 18:
    print('Eres un adulto')
else:
    print('No eres un adulto')

if age == 13:
    print('veo que tienes 13 años')

import sys

argumentos = sys.argv

if (len(argumentos) < 3):
    print('Error: Faltan argumentos')
    sys.exit(1)

texto = argumentos[1]
try:
    repeticiones = int(argumentos[2])
except ValueError:
    print('Error: El segundo argumento debe de ser un número entero')
    sys.exit(1)


for _ in range(repeticiones):
    print(texto)

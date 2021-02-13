import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', help='archivo a leer')
parser.add_argument('-l', '--line', help='linea a consultar')
args = parser.parse_args()

if not args.file or not args.line:
    print('Error: No se pudo completar porque faltan argumentos')
    sys.exit(1)


try:
    line_number = int(args.line)
except ValueError:
    print('Error: La línea debe ser un número entero')
    sys.exit(1)

try:
    with open(args.file) as file:
        lines = file.readlines()
        line = lines[line_number - 1]
        print(line, end='')
except IndexError:
    print('Error: La línea no existe en el archivo')
    sys.exit(1)

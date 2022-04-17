"""
6. Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla 
e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso, 
retorne qual o tipo de triângulo formado. Para que X, Y e Z formem um triângulo é necessário que a seguinte 
propriedade seja satisfeita: o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento 
dos outros dois lados. Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

    * Triângulo Equilátero: os comprimentos dos três lados são iguais.
    * Triângulo Isósceles: os comprimentos de dois lados são iguais.
    * Triângulo Escaleno: os comprimentos dos três lados são diferentes.
"""
import sys

fields = [
    {'label': 'Entre com o valor do lado X do triângulo": ', 'value': 0},
    {'label': 'Entre com o valor do lado Y do triângulo": ', 'value': 0},
    {'label': 'Entre com o valor do lado Z do triângulo": ', 'value': 0}
]

def get_triangle_type(x, y, z):
    if x == y and y == z:
        return 'Equilatero'
    elif x == y or y == z or x == z:
        return 'Isosceles'
    else:
        return 'Escaleno'


def main():

    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) <= 0):
                print('O valor informado não é válido!')
            else:
                break

    print(get_triangle_type(float(fields[0]['value']), float(fields[1]['value']), float(fields[2]['value'])))

if __name__ == "__main__":
    sys.exit(main())
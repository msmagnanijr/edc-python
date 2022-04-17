"""
1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive.
O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.
"""

import sys

fields = [
    {'label': 'Por favor, entre com o valor de "N": ', 'value': 0}
]

def sum_odd_number(n):
    sum = 0
    for i in range(0, n + 1):
        if (i % 2 != 0):
            sum += i
    return sum

def main():
    print('Vamos realizar a soma de todos os números ímpares de 1 até um dado "N"')
    print("\n")
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) <= 0):
                print('O valor informado não é válido!')
            else:
                break

    result = sum_odd_number(int(fields[0]['value']))
    print("\n")
    print(f'A soma de todos os números ímpares de 1 até {fields[0]["value"]} é {result}')

if __name__ == "__main__":
    sys.exit(main())
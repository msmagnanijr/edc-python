"""
7. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda. 
Assuma que a string tem pelo menos x caracteres. Isto é, utilizando como entradas a string “aeiou” e o inteiro 3, o resultado da sua função deve ser “ouaei”.
"""
import sys

fields = [
    {'label': 'Entre com a string que deverá ser rotacionada: ', 'value': ''},
    {'label': 'Entre com um numero inteiro: ', 'value': 0}
]

def get_string(fields):
    return fields[0]['value']

def get_number(fields):
    return int(fields[1]['value'])

def rotate_string(string, number):
    return string[number:] + string[:number]

def main():

    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ")
            if field['value'] != '':
                break
            else:
                print("Entre com algum valor!")

    print(f"String: {get_string(fields)}")
    print(f"Número: {get_number(fields)}")
    print(f"Rotacionada: {rotate_string(get_string(fields), get_number(fields))}")

if __name__ == "__main__":
    sys.exit(main())
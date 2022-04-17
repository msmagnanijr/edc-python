"""Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os."""
import sys

fields = [
    {'label': 'Por favor, entre com o valor do primeiro numero inteiro: ', 'value': 0},
    {'label': 'Por favor, entre com o valor do segundo numero inteiro: ', 'value': 0},
    {'label': 'Por favor, entre com o valor do terceiro numero inteiro: ', 'value': 0},
    {'label': 'Por favor, entre com o valor do quarto numero inteiro: ', 'value': 0},
    {'label': 'Por favor, entre com o valor do quinto numero inteiro: ', 'value': 0}
]

vector = []

def main():
    print("\n")
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) <= 0):
                print('O valor informado não é válido!')
            else:
                break
        vector.append(int(field['value']))

    print("Imprimindo o vetor: ", vector)

if __name__ == "__main__":
    sys.exit(main())
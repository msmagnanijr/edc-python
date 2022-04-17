"""
3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de N=0 é um. 
O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. 
Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.
"""
import sys

fields = [
    {'label': 'Entre comum número positivo para que o "Fatorial" seja calculado": ', 'value': 0}
]

def calc_fatorial(n):
    fatorial = 1
    for i in range(n, 1, -1):
        fatorial *= n
        n -= 1
    return fatorial

def main():

    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) < 0):
                print('Fatorial não é calculado com números negativos!')
            else:
                break
            
    result = calc_fatorial(int(field['value']))
    print(f'O fatorial de {field["value"]} é {result}')

if __name__ == "__main__":
    sys.exit(main())
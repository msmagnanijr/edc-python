"""
4. Escreva um programa em Python que calcule o fatorial de um dado número N usando um while. 
Use as mesmas especificações do item anterior.
"""
import sys

fields = [
    {'label': 'Entre comum número positivo para que o "Fatorial" seja calculado": ', 'value': 0}
]

def calc_fatorial(n):
    fatorial = 1
    while n > 1:
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
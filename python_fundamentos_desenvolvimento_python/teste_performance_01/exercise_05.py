"""
5. Trabalhar com tuplas é muito importante! Crie 4 funções nas quais:
    * Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o indice do mesmo
    * Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
    * Dada uma tupla e um elemento, elimine esse elemento da tupla.
    * Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.
"""
import sys

fields = [
    {'label': 'Entre com um elemente da seguinte tupla "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)": ', 'value': 0}
]

def find_element(tuple, element):
    for i, v in enumerate(tuple):
        if v == element:
            return i
    return -1

def split_tuple(tuple):
    half = len(tuple) // 2
    return tuple[:half], tuple[half:]

def reverse_tuple(tuple):
    return tuple[::-1]

def remove_element(tuple, element):
    return tuple[:tuple.index(element)] + tuple[tuple.index(element) + 1:]

def main():

    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) < 1 or float(field['value']) > 10):
                print('Esse elemento não existe na tupla!')
            else:
                break

    tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"{tuple}")
    index = find_element(tuple, int(field['value']))
    if index != -1:
        print(f'O elemento {field["value"]} existe na tupla e está na posição {index}')
    else:
        print(f'O elemento {field["value"]} não existe na tupla')
    print(f'Tupla original: {tuple}')
    print(f'Tupla com metade: {split_tuple(tuple)[0]} e {split_tuple(tuple)[1]}')
    print(f'Tupla invertida: {reverse_tuple(tuple)}')
    print(f'Tupla com elemento {field["value"]} eliminado: {remove_element(tuple, int(field["value"]))}')

if __name__ == "__main__":
    sys.exit(main())
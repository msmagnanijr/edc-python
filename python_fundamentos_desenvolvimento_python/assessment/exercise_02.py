"""Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive.
O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma."""

import sys

def main():

    try:
        n =  int(input('Digite um número inteiro: '))
        print(f'{n}')

        sum = 0
        for i in range(1, n+1):
            if i % 2 == 0:
                sum += i
        print(f'A soma dos números pares de 1 até {n} é {sum}')
    except ValueError:
        print('Valor inválido')
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
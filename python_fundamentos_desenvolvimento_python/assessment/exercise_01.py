"""Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros,
(n1, n2, n3) e os imprima em ordem crescente.
"""
import sys

def main():

    try:
        n1, n2, n3 = tuple(sorted(int(n) for n in input('Digite 3 números: ').split())[:3])
        print(f'{n1} {n2} {n3}')
    except ValueError:
        print('Valor inválido')
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
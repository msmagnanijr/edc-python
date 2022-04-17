"""Escreva uma função em Python que leia uma tupla contendo números inteiros,
retorne uma lista contendo somente os números ímpares e uma nova tupla contendo
somente os elementos nas posições pares."""
import sys

def odd_even(tuple):
    odd_list = []
    even_list = []
    for i in range(len(tuple)):
        if i % 2 == 0:
            even_list.append(tuple[i])
        else:
            odd_list.append(tuple[i])
    return odd_list, even_list

def main():
    print(odd_even((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

if __name__ == "__main__":
    sys.exit(main())
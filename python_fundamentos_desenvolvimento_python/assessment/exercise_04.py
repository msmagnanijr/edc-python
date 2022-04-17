"""Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa.
Imprima o vetor no final. Use listas. Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4]."""
import sys

def main():
    vetor = []
    for i in range(5):
        vetor.append(int(input("Digite um número: ")))
    print(vetor[::-1])

if __name__ == "__main__":
    sys.exit(main())
"""Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente.
Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele.
"""
import sys

fields = [
    {'label': 'Por favor, entre com o valor de "N": ', 'value': 0}
]

def main():
    vector_size = int(input("Digite o tamanho da lista: "))
    vector = []

    for i in range(0, vector_size):
        numbers = input("Entre com um número: ")
        vector.append(int(numbers))
    print(vector)

    if vector.__contains__(0):
        print("Existem ", vector.count(0), "ocorrências de zero na lista")
    else:
        print("Não existem ocorrências de zero na lista")
if __name__ == "__main__":
    sys.exit(main())
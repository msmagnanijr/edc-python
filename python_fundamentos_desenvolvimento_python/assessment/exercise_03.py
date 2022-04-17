"""Usando o Thonny, escreva uma função em Python chamada potencia.
Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB
usando multiplicações sucessivas (não use a função de python math.pow)
e retornar o resultado da operação.
Depois, crie um programa em Python que obtenha dois números inteiros do usuário
e indique o resultado de AB usando a função."""

import sys

def potencia():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    resultado = a
    for i in range(1, b):
        resultado = resultado * a
    return resultado

def main():
    print(potencia())

if __name__ == "__main__":
    sys.exit(main())
"""Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”."""

import re
import sys

sentences = []

def main():
    running = True
    while running:
        while True:
            data = input(f"Entre com uma frase: ")

            if data == 'sair':
                running = False
                break

            if not data:
                print(f"O valor informado é inválido")
            else:
                sentences.append(data)
                break

    for frase in sentences:
        if bool(re.search(r'\beu\b', frase.lower())):
            print(f"A frase \"{frase}\" possui a sentença \"eu\"")

if __name__ == "__main__":
    sys.exit(main())
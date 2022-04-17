"""Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura."""
import sys

def main():
    words = ["No", "meio", "do", "caminho", "tinha", "uma", "pedra", "tinha","uma","pedra"]
    words.reverse()
    print(words)

if __name__ == "__main__":
    sys.exit(main())
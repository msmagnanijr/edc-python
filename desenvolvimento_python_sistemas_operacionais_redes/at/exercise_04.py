"""Escreva um programa em Python que leia um arquivo texto e apresente na tela o seu conteúdo reverso."""
import sys

def revert_strings_in_file():
    filename = input('Enter filename: ')
    try:
        with open(filename, 'r') as f:
            for line in reversed(f.readlines()):
                print(line.rstrip()[::-1])
    except FileNotFoundError:
        print('File not found')
        sys.exit(1)

def main():
    revert_strings_in_file()

if __name__ == "__main__":
    sys.exit(main())
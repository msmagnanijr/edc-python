"""7. Escreva um programa que imprima apenas o caminho absoluto de um arquivo com nome relativo.
A impressão não deve conter o nome do arquivo, apenas o caminho."""

import sys
import os

def get_absolute_path(file_name):
    """
    Função que retorna o caminho absoluto de um arquivo
    """
    return  os.path.dirname(os.path.abspath(file_name))

def main():
    """
    Função principal
    """
    file_name = input("Digite o nome do arquivo: ")
    print(f"O caminho do arquivo {file_name} é: " + get_absolute_path(file_name))


if __name__ == '__main__':
    main()
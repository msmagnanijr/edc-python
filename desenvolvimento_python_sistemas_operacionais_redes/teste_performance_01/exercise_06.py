"""6. Escreva um programa que indique a extensão de um arquivo
usando a função do módulo os.path."""

import sys
from os import path

def check_extension(file_name):
    """
    Função que verifica a extensão de um arquivo
    """
    return path.splitext(file_name)[1]

def main():
    """
    Função principal
    """
    file_name = input("Digite o nome do arquivo: ")
    print(f"A extensão do arquivo {file_name} é: " + check_extension(file_name))


if __name__ == '__main__':
    main()
"""8. Escreva um programa que mostre a quantidade de bytes (em KB)
de cada arquivo em um diretório."""

import os
import sys
import enum

def print_file_size_in_directory(directory):
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            print(f"{file}: {file_size/1024} KB")

def main():
    """
    Função principal
    """
    dir = input("Digite o caminho do diretório: ")
    print(f"Exibindo o tamanho dos arquivos em KB no diretório {dir}")
    print_file_size_in_directory(dir)


if __name__ == '__main__':
    main()
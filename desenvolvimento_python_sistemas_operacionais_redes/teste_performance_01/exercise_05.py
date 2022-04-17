""" 5. Escreva um programa que indique se um arquivo existe ou não.
Caso exista, indique se é realmente um arquivo ou não."""

from os import path

def check_if_file_exists(file_name):
    if path.isfile(file_name):
        print("O 'arquivo' existe e é um arquivo.")
    elif path.isdir(file_name):
            print("O 'arquivo' existe e é um diretório.")
    else:
        print("O arquivo não existe.")

def main():
    file_name = input("Digite o nome do arquivo: ")
    check_if_file_exists(file_name)


if __name__ == '__main__':
    main()
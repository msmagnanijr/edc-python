"""9. Escreva um programa que mostre as datas de criação e
modificação de cada arquivo em um diretório.
"""
import os
import datetime
import time

def prit_creation_file_date(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            creation_date = time.ctime(os.path.getctime(file_path))
            print(f"{file_path} - {creation_date}")

def print_last_file_change_date(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            last_modified = time.ctime(os.path.getmtime(file_path))
            print(f"{file_path} - {last_modified}")

def main():
    """
    Função principal
    """
    dir = input("Digite o caminho do diretório: ")
    print(f"Exibindo a data de criação dos arquivos no diretório {dir}")
    prit_creation_file_date(dir)
    print("\n")
    print(f"Exibindo a data de modificação dos arquivos no diretório {dir}")
    print_last_file_change_date(dir)


if __name__ == '__main__':
    main()
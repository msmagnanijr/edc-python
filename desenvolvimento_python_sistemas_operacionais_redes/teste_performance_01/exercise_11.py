"""11. Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo,
usando o módulo ‘os’, de bloco de notas (notepad) para abri-lo.
"""
import os
import sys

def open_gedit(file_name):
    """
    Função para abrir o arquivo no gedit
    """
    #  this is the command to open the file in gedit (notepad)
    os.system(f"gedit {file_name}")

def main():
    """
    Função principal
    """
    file_name = input("Digite o caminho do arquivo de texto: ")
    open_gedit(file_name)

if __name__ == '__main__':
    main()
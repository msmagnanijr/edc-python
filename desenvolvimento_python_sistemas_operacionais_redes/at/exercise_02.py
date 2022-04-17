"""Escreva um programa que obtenha um nome de um arquivo texto do usuário e crie um processo para executar o
programa do sistema Windows bloco de notas (notepad) para abrir o arquivo."""

import sys
import subprocess
import os


supported_extensions = [".txt", ".doc", ".docx", ".odt", ".rtf", ".md"]

# linux editor
def open_editor(filename):
    subprocess.Popen(['gedit', filename])


def main():
    try:
        filename = input("Enter a filename: ")
        if os.path.isfile(filename) and filename.endswith(tuple(supported_extensions)):
            open_editor(filename)
        else:
            raise ValueError
    except ValueError as e:
        print("Invalid filename", e)

if __name__ == "__main__":
    sys.exit(main())
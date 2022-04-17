"""
1. Escreva um programa usando o módulo ‘os’ de Python que imprima o nome de usuário.
"""

import os
import pwd
import sys

def main():
    print("O nome do usuário 'logado' nessa sessão é: " + os.environ.get('USER'))

if __name__ == "__main__":
    sys.exit(main())
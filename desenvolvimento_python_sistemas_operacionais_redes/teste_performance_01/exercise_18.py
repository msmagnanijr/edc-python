"""18. Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB,
quanto de memória principal e quanto de memória de paginação (swap) existem no computador."""

import os
import psutil
from psutil._common import bytes2human

def main():

    print("Valor da Memória Principal: " + bytes2human(getattr(psutil.virtual_memory(), 'total')))
    print("Valor da Memória de Paginação: " + bytes2human(getattr(psutil.swap_memory(), 'total')))

if __name__ == '__main__':
    main()
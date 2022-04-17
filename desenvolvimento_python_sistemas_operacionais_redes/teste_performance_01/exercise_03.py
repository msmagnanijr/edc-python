"""3. Escreva um programa usando o módulo ‘os’ de Python que imprima o PID do próprio processo
e também seu GID (identificador de grupo) caso seja sistema do tipo Linux."""

import os
import sys


def get_current_platform():
    """
    Retorna o sistema operacional atual
    """
    return sys.platform

def get_current_os():
    """
    Retorna o sistema operacional atual
    """
    return os.name

def get_current_pid():
    """
    Retorna o PID do processo atual
    """
    return os.getpid()

def get_current_gid():
    """
    Retorna o GID do processo atual
    """
    return os.getgid()

def main():
    print(f'PID: {get_current_pid()}')
    if  get_current_os() == 'nt':
        print('Sistema Operacional Windows')
    elif get_current_os() == 'posix':
        print('Sistema Operacional Linux')
        print(f'GID: {get_current_gid()}')
    else:
        print('Sistema Operacional Desconhecido')

if __name__ == '__main__':
    main()
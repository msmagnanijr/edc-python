"""Associado à questão anterior, crie um programa servidor que:
Espere conexões UDP de processos na porta 9991.
Aguarde indefinidamente conexão de clientes.
Sirva cada cliente com a informação da quantidade total e disponível de armazenamento do disco principal 
(diretório corrente que o processo servidor está executando)."""

import socket
import sys

host = socket.gethostname()
port = 9991
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (host, port)

def get_available_space_current_directory_in_gigabytes():
    import os
    return os.statvfs('.').f_bavail * os.statvfs('.').f_frsize / 1024 / 1024 / 1024


def main():
    udp.bind(dest)
    while True:
        data, client_addr = udp.recvfrom(1024)
        print(f'Received {data} from {client_addr}')
        space = get_available_space_current_directory_in_gigabytes()
        udp.sendto(f'{space}'.encode('utf-8'), client_addr)

if __name__ == "__main__":
    sys.exit(main())

"""Escreva um programa cliente e servidor sobre TCP em Python em que:
O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta."""

import socket
import sys

target_host = socket.gethostname()
target_port = 9999

def configure_client_tcp_socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client

def list_server_directories_files(dir):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    client.send(dir.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listing server files: " , target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def main():

    while True:
        try:
            dir = input("Enter a directory: ")
            list_server_directories_files(dir)
        except KeyboardInterrupt:
            print("\n")
            print("Exiting...")
            sys.exit()

if __name__ == "__main__":
    sys.exit(main())

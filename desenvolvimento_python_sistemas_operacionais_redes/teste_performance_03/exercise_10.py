"""Crie um programa cliente que:
conecte-se a um servidor via TCP de mesmo IP e porta 8881.
Envie ao servidor o nome de um arquivo para que ele transmita este arquivo para o cliente.
Receba o tamanho do arquivo.
Se o tamanho for válido, receba o arquivo. Caso contrário, avise ao usuário que o arquivo não foi encontrado."""

import socket
import sys

host = socket.gethostname()
port = 8881
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)

def main():
    tcp.connect(dest)
    filename = input("Digite o nome do arquivo: ")
    tcp.send(filename.encode())
    size = tcp.recv(1024)
    if size.decode() == "0":
        print("Arquivo não encontrado")
    else:
        tcp.send("OK".encode())
        with open(filename, 'wb') as f:
            while True:
                data = tcp.recv(1024)
                if not data:
                    break
                f.write(data)
        print("Arquivo recebido com sucesso")

if __name__ == "__main__":
    sys.exit(main())

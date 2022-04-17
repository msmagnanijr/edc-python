"""Escreva um programa cliente e servidor sobre TCP em Python em que:
O cliente envia para o servidor o nome de um diretório e recebe a lista de arquivos (apenas arquivos) existente nele.
O servidor recebe a requisição do cliente, captura o nome dos arquivos no diretório em questão e envia a resposta ao cliente de volta."""

import socket
import sys
import os
import threading


bind_ip = socket.gethostname()
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*]  Listening at address: %s:%d" % (bind_ip, bind_port))

def get_list_of_files(directory):
    try:
        list_of_files = []
        for file in os.listdir(directory):
            list_of_files.append(file)
        files_string = " | ".join((list_of_files))
        return files_string
    except Exception as e:
        return str(e)

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)
        print("[*] Received: %s" % request)
        data = request.decode('utf-8')
        files = get_list_of_files(data)
        client_socket.send(files.encode('utf-8'))
        print(client_socket.getpeername())
        client_socket.close()
    except Exception as e:
        print(e)

def main():
    start_server()
    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    sys.exit(main())

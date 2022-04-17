"""Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor
e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta."""

import socket
import sys

target_host = socket.gethostname()
target_port = 9999

def configure_client_udp_socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)
    return client

def get_server_available_memory():
    try:
        client = configure_client_udp_socket()
        print("Type 'get_memory' to get the server available memory or 'exit' to finish the program")
        message =  input("Enter the message: ")
        client.sendto(message.encode('utf-8'), (target_host, target_port))
        if message == "exit":
            print("\n")
            print("Exiting...")
            client.close()
            sys.exit()
        else:
            attempts = 0
            while attempts < 5:
                try:
                    data, addr = client.recvfrom(4096)
                    print(data.decode('utf-8'))
                    break
                except socket.timeout:
                    attempts += 1
                    print("Request timed out, retrying...")
                    continue
            client.close()
    except KeyboardInterrupt:
        print("\n")
        print("Exiting...")
        client.close()
        sys.exit()


def main():
    get_server_available_memory()

if __name__ == "__main__":
    sys.exit(main())
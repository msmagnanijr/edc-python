"""Escreva um programa cliente e servidor sobre UDP em Python que:
O cliente envia para o servidor o pedido de obtenção da quantidade total e disponível de memória no servidor
e espera receber a resposta durante 5s. Caso passem os 5s, faça seu programa cliente tentar novamente mais 5 vezes (ainda esperando 5s a resposta) antes de desistir.
O servidor repetidamente recebe a requisição do cliente, captura a informação da quantidade total e disponível de memória há no servidor e envia a resposta ao cliente de volta."""


import socket
import sys
import psutil

bind_ip = socket.gethostname()
bind_port = 9999

def configure_client_udp_socket():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("[*]  Listening at address: %s:%d" % (bind_ip, bind_port))
    return client

def get_server_available_memory():
    try:
        while True:
            client = configure_client_udp_socket()
            client.bind((bind_ip, bind_port))
            data, addr = client.recvfrom(1024)
            client_input = data.decode('utf-8')
            if client_input == 'exit':
                print("\n")
                print("Exiting...")
                client.close()
                sys.exit()
            elif client_input == 'get_memory':
                print("[*]  Received data: %s" % data)
                print("[*]  Sending data back to the client")
                memory_info = psutil.virtual_memory()
                resposta = "Total Memory: " + str(memory_info.total/1048576) +" MB  |  Free Memory: " + str(memory_info.available/1048576) + " MB  |  " + str(100-memory_info.percent) + " %"
                client.sendto(str(resposta).encode(), addr)
                client.close()
            else:
                print("[*] No data received")
                sys.exit(0)
    except KeyboardInterrupt:
        print("\n")
        print("Exiting...")
        client.close()
        sys.exit()

def main():
        get_server_available_memory()

if __name__ == "__main__":
    sys.exit(main())
"""Crie um programa cliente que:
conecte-se a um servidor via UDP de mesmo IP e porta 9991.
Peça ao servidor que envie a quantidade total e disponível de armazenamento do disco principal.
Receba e exiba a informação."""


import socket
import sys

host = socket.gethostname()
port = 9991
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (host, port)

def main():
    udp.sendto(b'', dest)
    data, addr = udp.recvfrom(1024)
    print(data.decode('utf-8') + ' gigabytes')

if __name__ == "__main__":
    sys.exit(main())

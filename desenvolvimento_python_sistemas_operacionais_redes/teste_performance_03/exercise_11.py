"""Associado à questão anterior, crie um programa servidor que:
Espere conexões TCP de processos na porta 8881.
Aguarde indefinidamente conexão de clientes.
Receba a requisição do arquivo do cliente e envie o seu tamanho, caso o tenha encontrado. Em caso negativo, envie um valor inválido -1.
Envie o arquivo para o cliente, caso o encontre."""

import socket
import sys
import os

host = socket.gethostname()
port = 8881
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (host, port)

def main():
    tcp.bind(dest)
    tcp.listen(1)
    print('Servidor TCP esperando conexão em %s:%s' % dest)
    while True:
        conexao, cliente = tcp.accept()
        print('Conexão de %s:%s' % cliente)
        while True:
            msg = conexao.recv(1024)
            if not msg:
                break
            print('Mensagem recebida: %s' % msg.decode('utf-8'))
            if msg.decode('utf-8') == 'fim':
                conexao.send(b'fim')
                break
            if os.path.isfile(msg.decode('utf-8')):
                conexao.send(str(os.path.getsize(msg.decode('utf-8'))).encode('utf-8'))
            else:
                conexao.send(b'-1')
        conexao.close()

if __name__ == "__main__":
    sys.exit(main())

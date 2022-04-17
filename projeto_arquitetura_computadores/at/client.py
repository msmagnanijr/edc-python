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
    data = ["1", dir]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando os arquivos/diretórios do servidor: " , target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def list_server_file_permisions(file):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["2", file]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando as permissões do arquivo: ", file ," no servidor: ", target_host, target_port)
    print([(4, 'r - Read'), (2, 'w - Write'), (1, 'x - Execute')])
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def list_process_server(name):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["3", name]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando os processos no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def list_server_process_resources_consumption(pid):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["4", pid]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando o consumo de recursos do processo: ", pid, " no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def server_staggered_scheeduling():
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    client.send("5".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando chamadas escalonadas no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def list_all_server_processes():
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    client.send("6".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando todos os processos no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_network_interfaces():
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    client.send("7".encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando as interfaces de rede disponíveis no servidor: " , target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()


def get_server_network_interfaces_details(interface):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["8", interface]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando informações da interface de rede ", interface, "no servidor", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_server_ports(ip):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["9", ip]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Listando as portas disponíveis no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    #client.close()

def get_server_subnet_mask(ip):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["10", ip]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Obtendo máscara de rede do servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def scan_devices_in_network(subnet):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["11", subnet]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Escaneando a 'rede do servidor' em busca de dispositivos conectados: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_interface_consumption(interface):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["12", interface]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Obtendo consumo da interface de rede: ", interface, "no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def get_process_consumption(pid):
    client = configure_client_tcp_socket()
    client.connect((target_host, target_port))
    data = ["13", pid]
    data_s = ",".join(data)
    client.send(data_s.encode('utf-8'))
    response = client.recv(4096)
    print("\n")
    print("Obtendo consumo do processo: ", pid, "no servidor: ", target_host, target_port)
    print(response.decode('utf-8'))
    print("\n")
    client.close()

def menu():
    """
    Função que exibe o menu
    :return:
    """
    print("""
    1 - Listar arquivos de um diretório
    2 - Listar permissões de um arquivo
    3 - Listar processos por nome
    4 - Verificar consumo de um processo
    5 - Executar chamadas escalonadas
    6 - Listar todos os processos ( precisa ser executado como root)
    7 - Listar interfaces de rede disponíveis
    8 - Listar informações da interface de rede
    9 - Listar portas disponíveis por IP
    10 - Obter subnet por IP
    11 - Scannear dispositivos na rede
    12 - Obter consumo de recursos de rede
    13 - Obter consumo de recursos por processo
    15 - Sair
    """)

def main():

    menu()
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                dir = input("Digite o diretório: ")
                list_server_directories_files(dir)
            elif choice == 2:
                file = input("Digite o caminho completo do arquivo: ")
                print(list_server_file_permisions(file))
            elif choice == 3:
                name = input("Digite o nome do processo: ")
                list_process_server(name)
            elif choice == 4:
                pid = input("Digite o PID do processo: ")
                list_server_process_resources_consumption(pid)
            elif choice == 5:
                server_staggered_scheeduling()
            elif choice == 6:
                list_all_server_processes()
            elif choice == 7:
                get_network_interfaces()
            elif choice == 8:
                interface = input("Digite a interface: ")
                get_server_network_interfaces_details(interface)
            elif choice == 9:
                ip = input("Digite o IP: ")
                get_server_ports(ip)
            elif choice == 10:
                ip = input("Digite o IP: ")
                get_server_subnet_mask(ip)
            elif choice == 11:
                subnet = input("Digite a subnet (por exemplo: 192.168.1.0/24): ")
                scan_devices_in_network(subnet)
            elif choice == 12:
                interface = input("Digite a interface: ")
                get_interface_consumption(interface)
            elif choice == 13:
                pid = input("Digite o PID do processo: ")
                get_process_consumption(pid)
            elif choice == 15:
                sys.exit()
            else:
                print("Opção inválida")
            menu()
        except ValueError:
            print("Opção inválida")

if __name__ == "__main__":
    sys.exit(main())

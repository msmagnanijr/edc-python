import socket
import threading
import sys
import psutil
import os
import sched
import time
import ipaddress

bind_ip = "127.0.0.0"
bind_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def start_server():
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("[*] Escutando no endereço: %s:%d" % (bind_ip, bind_port))

def list_directories_files (path):
    list_files = []
    for file in os.listdir(path):
        list_files.append(file)
    files_string = " | ".join((list_files))
    return files_string

def list_file_permissions(path):
    mask = oct(os.stat(path).st_mode)[-3:]
    return mask

def list_process(name):
    process_list = []
    for proc in psutil.process_iter():
        if proc.name() == name:
            process_list.append("Nome: " + proc.name() + " Executável: " + proc.exe() + " PID: " + str(proc.pid))
    process_string = " | ".join((process_list))
    return process_string

def list_process_resources_consumption(pid):
    consumption_list = []
    consumption_list.append("Memória: " + str(round((psutil.Process(pid).memory_info().rss))/(1024*1024)) + "MB" + " | " +
        "CPU: " + str(round((psutil.Process(pid).cpu_percent()), 2)) + "%" + " | " + "Tempo de CPU: " + str(psutil.Process(pid).cpu_times()))
    consumption_string = " | ".join((consumption_list))
    return consumption_string

def staggered_scheeduling():

    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(1, 1, get_network_interfaces, ())
    scheduler.enter(2, 1, list_process, ("python3",))
    scheduler.run()
    end = time.time()
    total = abs(end - start)
    data = ("Finalizando as chamadas escalonadas..." + (f" Tempo total: {total:.0f} segundos"))
    return data

def list_all_processes():
    process_list = []
    for proc in psutil.process_iter():
        process_list.append("Nome: " + proc.name() + " Executável: " + proc.exe() + " PID: " + str(proc.pid))
    process_string = " | ".join((process_list))
    return process_string

def get_network_interfaces():
    interfaces =  []
    for interface in psutil.net_if_addrs():
        interfaces.append(interface)
    interfaces_string = " | ".join((interfaces))
    return interfaces_string

def get_network_interfaces_details(interface):
    data = []
    data.append("IPv4: " + psutil.net_if_addrs()[interface][0][1] + " | " + "IPv6: " + psutil.net_if_addrs()[interface][1][1] + " | " + "Máscara: " + psutil.net_if_addrs()[interface][0][2])
    data_string = " ".join((data))
    return data_string

def get_ports(ip):
    data = os.system(f"nmap -p- {ip}")
    return str(data)

def get_subnet_mask(ip):
    data = []
    net = ipaddress.ip_interface(ip)
    data.append("IP: " + str(net.ip) + " | " + "Mascara: " + str(net.netmask) + " | " +  "CIDR: " + str(net.network).split('/')[1] + " | " +  "Rede: " + str(net.network).split('/')[0] + " | " +  "Broadcast: " + str(net.network.broadcast_address))
    data_string = " ".join((data))
    return data_string

def scan_devices_in_network(subnet):
    data = []
    data.append(os.system(f"nmap -sP  {subnet}"))
    data_string = " ".join(str(data))
    return data_string

def get_interface_consumption(interface):
    data = []
    ipv4 = psutil.net_if_addrs()[interface][0][1]
    ipv6 = psutil.net_if_addrs()[interface][1][1]
    bytesecv = psutil.net_io_counters(pernic=True)[interface].bytes_recv
    bytesecs = psutil.net_io_counters(pernic=True)[interface].bytes_sent
    data.append("IPv4: " + ipv4 + " | " + "IPv6: " + ipv6 + " | " + "Bytes Recebidos: " + str(bytesecv) + " | " + "Bytes Enviados: " + str(bytesecs))
    data_string = " ".join((data))
    return data_string

def  get_process_consumption(pid):
    data = []
    memory = str("Memória" + str(round((psutil.Process(pid).memory_info().rss))/(1024*1024), "MB"))
    cpu = str("CPU: ", str(psutil.Process(pid).cpu_percent(), "%"))
    data.append(memory + " | " + cpu )
    data_string = " ".join((data))
    return data_string

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Recebido: %s" % request)
    request_data = request.decode('utf-8')
    data = request_data.split(",")
    if data[0] == "1":
        files = list_directories_files(data[1])
        client_socket.send(bytes(files, 'utf-8'))
    elif data[0] == "2":
        permission = list_file_permissions(data[1])
        client_socket.send(bytes(permission, 'utf-8'))
    elif data[0] == "3":
        process = list_process(data[1])
        client_socket.send(bytes(process, 'utf-8'))
    elif data[0] == "4":
        consumption = list_process_resources_consumption(int(data[1]))
        client_socket.send(bytes(consumption, 'utf-8'))
    elif data[0] == "5":
        data = staggered_scheeduling()
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "6":
        data = list_all_processes()
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "7":
        interfaces = get_network_interfaces()
        client_socket.send(bytes(interfaces, 'utf-8'))
    elif data[0] == "8":
        data = get_network_interfaces_details(data[1])
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "9":
        data = get_ports(data[1])
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "10":
        data = get_subnet_mask(data[1])
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "11":
        data = scan_devices_in_network(data[1])
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "12":
        data = get_interface_consumption(data[1])
        client_socket.send(bytes(data, 'utf-8'))
    elif data[0] == "13":
        data = get_process_consumption(int(data[1]))
        client_socket.send(bytes(data, 'utf-8'))
        sys.exit()
    print(client_socket.getpeername())
    client_socket.close()

def main():
    start_server()
    while True:
        client, addr = server.accept()
        print("[*] Nova conexão realizada pelo cliente %s:%d" % (addr[0], addr[1]))
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    sys.exit(main())

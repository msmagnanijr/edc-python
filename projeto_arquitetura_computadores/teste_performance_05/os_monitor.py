import psutil
import os
import sys
import sched
import time

def list_dir_files(path):
    """
    Função que lista os arquivos/diretórios de um diretório
    :param path:
    :return:
    """
    list_files = []
    for file in os.listdir(path):
        list_files.append(file)
    return list_files

def list_permissions(path):
    """
    Função que lista as permissões de um arquivo
    :param path:
    :return:
    """
    print([(4,"r - Read"),(2,"w - Write"),(1,"x - Execute")])
    mask = oct(os.stat(path).st_mode)[-3:]
    return mask

def list_processes():
    """
    Função que lista todos os processos
    :return:
    """
    # Lista os processos
    for proc in psutil.process_iter():
        try:
            print(proc.name(), proc.exe(), proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def list_processes_by_name(name):
    """
    Função que lista os processos por nome
    :param name:
    :return:
    """
    # Lista os processos
    for proc in psutil.process_iter():
        try:
            if proc.name() == name:
                print(proc.name(), proc.exe(), proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def list_resources_by_process(pid):
    """
    Função que lista os recursos de um processo
    :param pid:
    :return:
    """
    # Lista consumo de memória e cpu
    print("Memória: ", round((psutil.Process(pid).memory_info().rss))/(1024*1024), "MB")
    print("CPU: ", psutil.Process(pid).cpu_percent(), "%")
    print(psutil.Process(pid).cpu_times())

def main_loop():
    """
    Função que executa o programa
    :return:
    """
    start = time.time()
    print("Iniciando as chamadas escalonadas.")
    # Cria o scheduler
    scheduler = sched.scheduler(time.time, time.sleep)
    # Cria o loop
    scheduler.enter(1, 1, list_processes, ())
    scheduler.enter(2, 1, list_processes_by_name, ("python3",))
    # Executa o loop
    scheduler.run()
    end = time.time()
    print("Finalizando as chamadas escalonadas.")
    total = abs(end - start)
    print(f"Tempo total: {total:.0f} segundos")

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
    6 - Listar todos os processos
    7 - Sair
    """)

def main():
    """
    Função principal
    :return:
    """
    menu()
    while True:
        try:
            choice = int(input("Escolha uma opção: "))
            if choice == 1:
                dir = input("Digite o diretório: ")
                print(list_dir_files(dir))
            elif choice == 2:
                file = input("Digite o caminho completo do arquivo: ")
                print(list_permissions(file))
            elif choice == 3:
                name = input("Digite o nome do processo: ")
                list_processes_by_name(name)
            elif choice == 4:
                pid = int(input("Digite o PID do processo: "))
                list_resources_by_process(pid)
            elif choice == 5:
                main_loop()
            elif choice == 6:
                list_processes()
            elif choice == 7:
                sys.exit()
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")

if __name__ == "__main__":
    sys.exit(main())
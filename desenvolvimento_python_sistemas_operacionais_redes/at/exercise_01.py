"""Escreva um programa em Python que:
obtenha a lista de processos executando no momento, considerando que o processo pode deixar de existir enquanto seu programa manipula suas informações;
imprima o nome do processo e seu PID;
imprima também o percentual de uso de CPU e de uso de memória."""

import psutil
import sys

def get_process_list():
    return psutil.pids()


def main():
    process_list = get_process_list()
    for pid in process_list:
        if pid != 0:
            try:
                process = psutil.Process(pid)
                print(f"Process name: {process.name()}")
                print(f"Process ID: {pid}")
                print(f"Percentage of CPU usage: {process.cpu_percent()}")
                print(f"Percentage of memory usage: {process.memory_percent()}")
            except Exception as e:
                print("An exception occurred" + e)

if __name__ == "__main__":
    sys.exit(main())
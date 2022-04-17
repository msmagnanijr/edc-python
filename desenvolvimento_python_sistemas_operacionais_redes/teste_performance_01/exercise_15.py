"""15. Escreva uma função em Python que, dado um número PID, imprima o nome do usuário proprietário,
o tempo de criação e o uso de memória em KB."""

import time
import psutil

def print_pid_info(pid):
    """Prints the owner, creation time and memory usage of a given process."""
    process = psutil.Process(pid)
    print('Proprietário:', process.username())
    print('Data de criação:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(process.create_time())))
    print('Uso da memória em KB:', process.memory_info().rss / 1024)

def main():
    pid = int(input('Digite o PID: '))
    print_pid_info(pid)

if __name__ == '__main__':
    main()
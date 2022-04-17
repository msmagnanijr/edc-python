"""16. Escreva um programa em Python, usando o módulo ‘psutil’, que imprima o tempo de CPU em segundos por núcleo."""

import time
import psutil

def print_cpu_time_in_seconds_per_core():
    times_cpu = psutil.cpu_times_percent(interval=1, percpu=True)
    for core in range(len(times_cpu)):
        print('{}Núcleo {}: user={} system={} idle={}'.format(' '*3,core, times_cpu[core][0], times_cpu[core][1],times_cpu[core][2]))

def main():
    print_cpu_time_in_seconds_per_core()

if __name__ == '__main__':
    main()
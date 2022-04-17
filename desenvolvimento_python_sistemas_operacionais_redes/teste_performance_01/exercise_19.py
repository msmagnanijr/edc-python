"""19. Escreva um programa em Python, usando o módulo ‘psutil’, que imprima em GB, quanto de armazenamento
disponível há na partição do sistema (onde o sistema está instalado)."""

import psutil
from psutil._common import bytes2human

def main():
    partitions = psutil.disk_partitions()
    usage = psutil.disk_usage(partitions[0][0])
    print(partitions)
    print('Partição do sistema {}\n\tArmazenamento disponível: {}'.format(partitions[0][0], bytes2human(usage[2])))

if __name__ == '__main__':
    main()
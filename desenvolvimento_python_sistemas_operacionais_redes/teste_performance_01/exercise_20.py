"""20. Escreva um programa em Python usando o módulo ‘psutil’, que imprima para a partição corrente:
o nome do dispositivo,
o tipo de sistema de arquivos que ela possui (FAT, NTFS, EXT, ...),
o total de armazenamento em GB e
o armazenamento disponível em GB."""

import psutil
from psutil._common import bytes2human

def get_device_name():
    """
    Function to get device name
    """
    return psutil.disk_partitions()[0].device

def get_disk_type(partition):
    """
    Function to get disk type
    """
    return psutil.disk_io_counters(perdisk=True)[partition].optype

def get_disk_info_human(partition):
    """
    Function to get disk info in human readable format
    """
    disk = psutil.disk_usage(partition)
    return disk.total, bytes2human(disk.free)

def main():
    """
    Main function
    """
    partition = get_device_name()
    disk_type = get_disk_type(partition)
    total, free = get_disk_info_human(partition)
    print(f'{partition} {disk_type} {total} {free}')

if __name__ == '__main__':
    main()
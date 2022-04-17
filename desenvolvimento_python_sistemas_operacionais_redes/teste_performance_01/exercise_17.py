"""17. Escreva um programa em Python, usando o módulo ‘psutil’, que imprima 20 vezes,
de segundo a segundo, o percentual do uso de CPU do computador."""

import psutil
import time
import sys
import os


def print_cpu_percent():
    for i in range(20):
        print(f"{psutil.cpu_percent()}%")
        time.sleep(1)


def main():
    print_cpu_percent()

if __name__ == '__main__':
    main()
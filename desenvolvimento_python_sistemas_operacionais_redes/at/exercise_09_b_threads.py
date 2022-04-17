"""Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos.
Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes)."""

import sys
import time
import threading
import threading,time
import random

vector = []
vector_result = []

def factorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def append_threading(vector, factorial,vector_result):
    for n in vector:
        vector_result.append(factorial(n))

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def running_threads():
    try:

        n = 1000000
        for i in range (n):
            vector.append(random.randint(0,100))

        size = len(vector)

        thread_0 = threading.Thread(target=append_threading, args=(vector[0:int(size/4)], factorial, vector_result))
        thread_0.start()

        thread_1 = threading.Thread(target=append_threading, args=(vector[int(size/4):int(size/3)], factorial, vector_result))
        thread_1.start()

        thread_2 = threading.Thread(target=append_threading, args=(vector[int(size/3):int(size/2)], factorial, vector_result))
        thread_2.start()

        thread_3 = threading.Thread(target=append_threading, args=(vector[int(size/2):size], factorial, vector_result))
        thread_3.start()

        thread_0.join()
        thread_1.join()
        thread_3.join()
        thread_3.join()

    except Exception as e:
        print(e)

def main():
    print("\nExecuting threads...")
    print("Time: {} seconds".format(calculate_time(running_threads)))


if __name__ == "__main__":
    sys.exit(main())
"""Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos.
Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes)."""

import multiprocessing
import sys
import time
import random

vector = []
vector_result = []

output = multiprocessing.Queue()

def factorial(n):
    f = n
    for i in range(n-1,1,-1):
        f = f * i
    return(f)

def append_processing(vector, factorial, vector_result, output):
    for n in vector:
        output.put(factorial(n))

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def running_process():

    try:

        n = 1000000
        for i in range (n):
            vector.append(random.randint(0,100))

        size = len(vector)


        process_0 = multiprocessing.Process(target=append_processing, args=(vector[0:1], factorial, vector_result, output))
        process_0.start()

        process_1 = multiprocessing.Process(target=append_processing, args=(vector[1:2], factorial, vector_result, output))
        process_1.start()

        process_2 = multiprocessing.Process(target=append_processing, args=(vector[2:3], factorial, vector_result, output))
        process_2.start()

        process_3 = multiprocessing.Process(target=append_processing, args=(vector[3:size], factorial, vector_result, output))
        process_3.start()

        while len(vector) != len(vector_result):
            vector_result.append(output.get())

        process_0.join()
        process_1.join()
        process_2.join()
        process_3.join()
    except Exception as e:
        print("Error: {}".format(e))

def main():
    print("\nExecuting multiprocessing...")
    print("Time: {} seconds".format(calculate_time(running_process)))
    print("\n")

if __name__ == "__main__":
    sys.exit(main())
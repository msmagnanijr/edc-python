
"""Escreva 3 programas em Python que resolva o seguinte problema:
Dado um vetor A de tamanho N com apenas números inteiros positivos, calcule o fatorial de cada um deles e armazene o resultado em um vetor B.

Para calcular o fatorial, utilize a seguinte função:


  def fatorial(n):
  fat = n
  for i in range(n-1,1,-1):
    fat = fat * i
  return(fat)


Os modos de desenvolver seu programa devem ser:

sequencialmente (sem concorrência);
usando o módulo threading com 4 threads;
usando o módulo multiprocessing com 4 processos."""

import sys
import time
import threading
import threading,time

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vector_result = []

def factorial(n):
    fat = n
    for i in range(n-1,1,-1):
        fat = fat * i
    return(fat)

def append_threading(vector, factorial,vector_result):
    for n in vector:
        vector_result.append(factorial(n))

def main():
    try:
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

        print("Calculating factorials 4 threads...")
        print("Original vector: {}".format(vector))
        print("Factorial vector: {}".format(vector_result))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    sys.exit(main())
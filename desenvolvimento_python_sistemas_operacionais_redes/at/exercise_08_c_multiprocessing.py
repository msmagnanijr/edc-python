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

import multiprocessing
import sys

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
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

def main():

    try:
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
        print("Calculating factorials multiprocessing...")
        print("Original vector: {}".format(vector))
        print("Factorial vector: {}".format(vector_result))
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    sys.exit(main())
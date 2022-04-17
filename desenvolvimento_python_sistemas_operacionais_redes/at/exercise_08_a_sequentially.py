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

import time
import sys
import random

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vector_result = []

def factorial(n):
  f = n
  for i in range(n-1,1,-1):
    f = f * i
  return(f)

def main():
    try:
        vector_result = []
        for i in vector:
            vector_result.append(factorial(i))
        print("Calculating factorials sequentially...")
        print("Original vector: {}".format(vector))
        print("Factorial vector: {}".format(vector_result))
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    sys.exit(main())
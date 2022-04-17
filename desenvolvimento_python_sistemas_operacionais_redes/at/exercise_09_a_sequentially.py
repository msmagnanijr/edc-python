"""Teste todos os 3 programas da questão 8, capture os tempos de execução deles e compare-os, explicando os resultados de tempos.
Varie o valor de N em 1.000.000, 5000.000, 10.000.000 (ou escolha números maiores ou melhores de acordo com a velocidade de processamento do computador utilizado para testes)."""

import time
import sys
import random

vector = []
vector_result = []

def factorial(n):
  f = n
  for i in range(n-1,1,-1):
    f = f * i
  return(f)

def calculate_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start

def running_sequentially():
    try:
        n = 1000000
        for i in range (n):
            vector.append(random.randint(0,100))

        for n in vector:
            vector_result.append(factorial(n))

    except KeyboardInterrupt:
        sys.exit()


def main():
    print("\nExecuting sequentially...")
    print("Time: {} seconds".format(calculate_time(running_sequentially)))

if __name__ == "__main__":
    sys.exit(main())
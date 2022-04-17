"""Faça uma função um programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios,
simulando os lançamentos dos dados. (código)"""

import random
import sys

scrolls = 100
results = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0
}

def main(scrolls):
    for n in range(0, scrolls):
        result = random.randint(1, 6)

        results[f"{result}"] += 1

    for side in results:
        print(f"O número {side} teve {results[side]} ocorrência{'s' if results[side] > 1 else ''}.")


if __name__ == "__main__":
    sys.exit(main(scrolls))

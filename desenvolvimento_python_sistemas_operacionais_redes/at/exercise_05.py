"""Escreva um programa em Python que leia dois arquivos, a.txt e b.txt, como a seguir:
 a.txt
 1 15 -42 33 -7 -2 39 8
 b.txt
 19 56 -43 23 -7 -11 33 21 61 9
 Seu programa deve somar elemento por elemento de cada arquivo e imprimir o resultado na tela.
 Isto é, o primeiro elemento de a.txt deve ser somado ao primeiro elemento de b.txt, segundo elemento de a.txt
 deve ser somado ao segundo elemento de b.txt, e assim sucessivamente. Caso um arquivo tenha mais elementos que o outro,
 os elementos que sobrarem do maior devem ser somados a zero."""

import sys


def check_index(index, list_size):
    if index < list_size:
        return True
    else:
        return False

def main():

    try:
        file_a = open("a.txt", "r").readlines()
        file_b = open("b.txt", 'r').readlines()

        print(f'Arquivo a: {file_a} | Arquivo b: {file_b}')
        print('-' * 85)

        for numbers in file_a:
            a =  numbers.split()

        for numbers in file_b:
            b = numbers.split()

        for i in range(10):
            if i < len(a):
                print("{} + {} = {}".format(a[i], b[i], int(a[i]) + int(b[i])))
            else:
                if(check_index(i, len(a))):
                    print("{} + {} = {}".format(a[i], 0, int(a[i]) + 0))
                else:
                    print("{} + {} = {}".format(0, b[i], 0 + int(b[i])))
    except Exception as e:
        print(e)
    finally:
        file_a.close()
        file_b.close()

if __name__ == "__main__":
    sys.exit(main())
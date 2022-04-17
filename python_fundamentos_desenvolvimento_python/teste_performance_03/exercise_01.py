"""Usando Python, faça o que se pede (código):
Crie uma lista vazia;
Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
Imprima a lista;
Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
Imprima a lista modificada;
Imprima também o tamanho da lista usando a função len();
Altere o valor do último elemento para 6 e imprima a lista modificada.
"""
import sys

def main():

    #Crie uma lista vazia
    list = []

    #Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
    list.extend((1,2,3,4,5))

    # Imprima a lista;
    print("Lista preenchida: ", list)

    # Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
    for indice in range(len(list) -1 ):
        if list[indice] == 3 or list[indice] == 6:
            del(list[indice])

    # Imprima a lista modificada;
    print("Lista modificada: ", list)

    # Imprima também o tamanho da lista usando a função len();
    print("Tamanho da Lista: ", len(list))

    # Altere o valor do último elemento para 6 e imprima a lista modificada.

    list.append(6)
    print("Lista modificada novamente: ", list)


if __name__ == "__main__":
    sys.exit(main())
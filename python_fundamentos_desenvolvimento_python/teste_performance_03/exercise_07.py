"""
Escreva um programa em Python que realiza operações de inclusão e remoção em listas.
Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
Mostrar lista;
Incluir elemento;
Remover elemento;
Apagar todos os elementos da lista.
Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista.
Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído.
Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido.
E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.
"""
import sys

elements = ["Cacau", "Guri", "Dakota"]

def show_list(list):
    print("\n\n")
    print(list)
    print("\n\n")

def add_lista(list, object):
    return list.append(object)

def remove_list(lista, object):
    return list.remove(object)

def del_list(list):
    for i in list:
        return list.pop()

def main(list):

    fechar = False

    while not fechar:
        print("Escolha as seguintes opcoes:\n"
        "(a) para mostrar a lista.\n"
        "(b) para incluir um elemento a lista.\n"
        "(c) para remover um elemento da lista.\n"
        "(d) para excluir todos os elementos da lista.\n"
        "(Sair) para sair do programa.\n")

        entrada = str(input("Entre com seu comando: "))

        if entrada == "a" or entrada == "A":
            show_list(list)
        elif entrada == "b" or entrada == "B":
            objeto = input("Entre com o objeto a ser adicionado na lista: ")
            add_lista(list, objeto)
        elif entrada == "c" or entrada == "C":
            objeto = input("Entre com o objeto a ser removido da lista: ")
            remove_list(list, objeto)
        elif entrada == "d" or entrada == "D":
            del_list(list)
            print("Operacao concluida!")
        elif entrada == "sair" or entrada == "Sair":
            fechar = True
        else:
            print("Comando invalido!")


if __name__ == "__main__":
    sys.exit(main(elements))

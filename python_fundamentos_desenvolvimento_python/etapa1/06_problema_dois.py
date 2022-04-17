import sys

fields = [
    {'label': 'Entre com um número: ', 'value': 0}
]


def main():
    numeros = []
    for field in fields:
        while (len(numeros) <= 4):
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
               or float(field['value']) <= 0):
                print("O valor informado não é válido!")
            else:
                numeros.append(int(field['value']))

    menor = numeros[0]

    for numero in numeros:
        if(menor > numero):
            menor = numero

    print(f"O menor número é {menor}")


if __name__ == "__main__":
    sys.exit(main())

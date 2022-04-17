import sys

fields = [
    {'label': 'Entre com a letra F ou M: ', 'value': ''}
]


def main():
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ")
            if not field['value']:
                print("O valor informado não é válido!")
            else:
                break

    genero = (fields[0]['value'])
    if genero.upper() == 'M':
        print('Masculino')
    elif genero.upper() == 'F':
        print('Feminino')
    else:
        print('Outro gênero!')


if __name__ == "__main__":
    sys.exit(main())

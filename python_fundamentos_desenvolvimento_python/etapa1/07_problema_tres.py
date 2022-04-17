import sys

fields = [
    {'label': 'Entre com um número: ', 'value': 0}
]


def main():
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
               or float(field['value']) <= 0):
                print("O valor informado não é válido!")
            elif float(field['value']) <= 10 and float(field['value']) > 0:
                print('Ok. Nota válida')
                print(float(field['value']))
            else:
                print(float(field['value']))
                print('Nota inválida')
                break


if __name__ == "__main__":
    sys.exit(main())

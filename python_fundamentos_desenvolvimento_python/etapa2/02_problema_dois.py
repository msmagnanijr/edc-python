import sys

fields = [
    {'label': 'Entre com sua idade: ', 'value': 0}
]


def calculate_resources():


def main():
    for field in fields:
    while True:
        field['value'] = input(f"{field['label']} ") or '0'
        if(not field['value'].replace(',', '').replace('.', '').isnumeric()
                or float(field['value']) <= 0):
            print("O valor informado não é válido!")
        else:
            break

    calculate_resources(float(field['value']))


if __name__ == "__main__":
    sys.exit(main())

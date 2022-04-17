import sys

fields = [
    {'label': 'Entre com sua idade: ', 'value': 0}
]


def go_drink(idade):
    if idade >= 18:
        print("Você pode beber bebida alcoólica")
        if(idade >= 21):
            print("Você é VIP!")
    else:
        print("Você pode beber água ou refrigerante")


def main():
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()or float(field['value']) <= 0):
                print("O valor informado não é válido!")
            else:
                break

    go_drink(float(field['value']))


if __name__ == "__main__":
    sys.exit(main())

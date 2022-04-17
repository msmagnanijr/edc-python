import sys

fields = [
    {'label': 'Entre com uma letra: ', 'value': ''}
]


def main():
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ")
            if not field['value']:
                print("O valor informado não é válido!")
            else:
                break

    palavra_original = (fields[0]['value'])

    palavra_final = palavra_original.lower()

    if palavra_original.isalpha():
        if palavra_final in 'aeiou':
            print("Vogal")
        else:
            print("Consoante")
    else:
        print("Nao é palavra!")


if __name__ == "__main__":
    sys.exit(main())

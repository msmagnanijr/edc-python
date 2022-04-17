import turtle
import sys

fields = [
    {'label': 'Olá! Quantos passos a tartaruga dará?', 'value': 0}
]


def go_turtle(distancia):
    turtle.title('Primeiro Programa')
    turtle.shape('turtle')
    turtle.forward(distancia)
    turtle.done()


def main():
    for field in fields:
        while True:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
               or float(field['value']) <= 0):
                print("O valor informado não é válido!")
            else:
                break

    go_turtle(int(fields[0]['value']))


if __name__ == "__main__":
    sys.exit(main())

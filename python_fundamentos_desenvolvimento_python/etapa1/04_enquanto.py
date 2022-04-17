import turtle
import sys

fields = [
    {'label': 'Indique o ângulo: ', 'value': 0}
]

# global scope
infnet_turtle = turtle.Turtle()
infnet_turtle.shape("turtle")


def drawing(angulo):
    infnet_turtle.left(angulo)
    infnet_turtle.forward(50)


def main():
    for field in fields:
        angulo = 0
        while angulo >= 0:
            field['value'] = input(f"{field['label']} ") or '0'
            if(not field['value'].replace(',', '').replace('.', '').isnumeric()
               or float(field['value']) <= 0):
                print("O valor informado não é válido!")
            else:
                drawing(int(field['value']))


if __name__ == "__main__":
    sys.exit(main())
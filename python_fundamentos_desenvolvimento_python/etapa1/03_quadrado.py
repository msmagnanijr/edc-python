import turtle
import sys


def drawing_square():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(2)
    for i in range(0, 4):
        brad.forward(100)
        brad.left(90)

    window.exitonclick()


def main():
    drawing_square()


if __name__ == "__main__":
    sys.exit(main())

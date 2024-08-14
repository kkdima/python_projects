import turtle
import random

turtle1 = turtle.Turtle()


def move_forwards():
    turtle1.forward(10)


def move_backwards():
    turtle1.backward(10)


def turn_left():
    turtle1.left(10)


def turn_right():
    turtle1.right(10)


def clear():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()


def main():
    # Set up turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.setup(width=500, height=400)

    screen.listen()
    screen.onkey(move_forwards, "Up")
    screen.onkey(move_backwards, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    screen.onkey(clear, "c")

    screen.exitonclick()


if __name__ == "__main__":
    main()

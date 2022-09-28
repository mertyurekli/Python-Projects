import turtle
from turtle import Turtle, Screen
from random import randint, randrange

painter = Turtle()
painter.shape("turtle")
painter.color("green")
painter.speed("fastest")

turtle.colormode(255)
#painter.pensize(10)

for _ in range(72):
    painter.pencolor(randint(1, 255), randint(1, 255), randint(1, 255))
    painter.circle(100, 360)
    painter.right(5)

screen = Screen()
screen.exitonclick()

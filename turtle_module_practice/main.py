import turtle
from turtle import Screen
import random

tim = turtle.Turtle()
turtle.colormode(255)


def draw_shape(side):
    angle = 360 / side
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup


######################################Random_Path_Generator############################################
# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(200)
#
# for _ in range(500):
#     tim.pencolor(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(20)


######################################_Spirograph_###################################################

# tim.speed('fastest')
# for i in range(361):
#     tim.pencolor(random_color())
#     tim.setheading(i)
#     tim.circle(1000)

#####################################################################################################
screen = Screen()
screen.exitonclick()

from turtle import Turtle, Screen
import random

########################################Etch_A_sketch#################################################
# tim = Turtle()
# screen = Screen()
# def move_forward():
#     tim.forward(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def clockwise():
#     tim.setheading(tim.heading()-10)
#
#
# def anticlockwise():
#     tim.setheading(tim.heading()+10)
#
#
# screen.listen()
#
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key='s', fun=move_backward)
# screen.onkey(key='c', fun=clear_screen)
# screen.onkey(key='d', fun=clockwise)
# screen.onkey(key='a', fun=anticlockwise)
############################################################################################################

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']
y_positions = [-100, -60, -20, 20, 60, 100]
diff_turtles = []


for turtle_index in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    diff_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in diff_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"You Won! {turtle.pencolor()} is the winner.")
            else:
                print(f"You Lost! {turtle.pencolor()} is the winner.")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()

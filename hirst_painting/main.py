import turtle as turtle_module
import random

turtle_module.colormode(255)

# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(color_list)

color_list = [(29, 105, 164), (227, 157, 67), (231, 214, 92), (188, 42, 84), (219, 138, 172), (140, 105, 57),
              (113, 185, 211), (217, 72, 98), (200, 168, 33), (157, 25, 65), (116, 191, 155), (24, 54, 129),
              (15, 182, 150), (106, 108, 192), (237, 89, 50), (140, 209, 226), (21, 141, 89), (19, 165, 204),
              (229, 165, 187), (83, 43, 29), (99, 49, 36), (23, 42, 80), (21, 90, 83), (237, 209, 7), (27, 85, 90),
              (102, 13, 47)]

tim = turtle_module.Turtle()
tim.penup()
tim.hideturtle()
tim.speed('fastest')

current_position = -250.00

for _ in range(10):
    tim.setposition(-250.00, current_position)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    current_position += 50

screen = turtle_module.Screen()
screen.exitonclick()
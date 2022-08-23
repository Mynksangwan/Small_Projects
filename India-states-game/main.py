import turtle
import pandas

screen = turtle.Screen()
screen.screensize(canvwidth=1024, canvheight=1237)
screen.title("Name the States and Union Territories")

image = 'india-blank-map-with-neighbouring-countries.gif'
screen.addshape(image)
turtle.shape(image)

# code to get coordinates of mouse clicking
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

data = pandas.read_csv("28_Indian_states&8_Union_Territories.csv")
all_states = data.state.to_list()
count = 0
guessed_states = []

while len(guessed_states) < 36:
    answer_state = screen.textinput(title=f"{count}/36 Correct", prompt="What's another state's name?").title()
    if answer_state in all_states:
        guessed_states.append(answer_state)
        count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color('red')
        state_data = data[answer_state == data.state]
        t.goto(x=float(state_data.x), y=float(state_data.y))
        t.write(answer_state, font=("Arial", 12, "normal"))

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break



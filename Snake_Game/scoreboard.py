from turtle import Turtle
ALIGN = 'center'
FONT = ('Arial', 16, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over!", align=ALIGN, font=FONT)

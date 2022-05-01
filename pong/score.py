from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score}:{self.r_score}",
                   align=ALIGNMENT, font=FONT)

    def update_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def update_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

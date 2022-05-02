from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 26, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} / Highscore: {self.highscore}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            with open("highscore.txt", "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_highscore()
        self.update_scoreboard()
        

    def update_highscore(self):
        with open("highscore.txt") as file:
            contents = file.read()
            self.highscore = int(contents)

#   def game_over(self):
#       self.goto(0, 0)
#       self.write("GAME OVER", align=ALIGNMENT, font=FONT)

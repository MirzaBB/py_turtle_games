from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.ycoord = -280
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.tilt(90)
        self.goto(STARTING_POSITION)

    def up(self):
        self.ycoord += MOVE_DISTANCE
        self.goto(0, self.ycoord)

    def game_over(self):
        self.goto(STARTING_POSITION)

    def next_level(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.ycoord = self.ycor()
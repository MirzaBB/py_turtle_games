from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xcoord):
        super().__init__()
        self.xcoord = xcoord
        self.ycoord = 0
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(self.xcoord, 0)

    def go_up(self):
        self.ycoord += 20
        self.goto(self.xcoord, self.ycoord)

    def go_down(self):
        self.ycoord -= 20
        self.goto(self.xcoord, self.ycoord)

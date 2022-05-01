from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("white")
        self.penup()
        self.x_move = 3
        self.y_move = 2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_colision(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1

    def increase_speed(self):
        if self.x_move > 0:
            self.x_move += 1
        else:
            self.x_move -= 1

    def reset_speed(self):
        if self.x_move > 0:
            self.x_move = 3
        else:
            self.x_move = -3

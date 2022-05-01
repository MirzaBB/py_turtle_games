from operator import indexOf
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        random_chance = random.randint(1, 20)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(f"{random.choice(COLORS)}")
            new_car.penup()
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.goto(320, random.randrange(-240, 280, 20))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def del_car(self):
        for car in self.all_cars:
            if car.xcor() <= -350:
                car.hideturtle()
                self.all_cars.pop(self.all_cars.index(car))

    def game_over(self):
        for car in self.all_cars:
            self.all_cars.clear
            car.hideturtle()

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.001)
    screen.update()

    car_manager.spawn_car()
    car_manager.move_cars()
    car_manager.del_car()

    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            car_manager.game_over()
            scoreboard.game_over()
            player.game_over()
            game_is_on = False

    if player.ycor() >= 280:
        scoreboard.update_level()
        player.next_level()
        car_manager.next_level()

screen.exitonclick()

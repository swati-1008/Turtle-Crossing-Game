from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
loop_index = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # Detect collision with car
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line
    if player.ycor() > 280:
        player.start()
        car.level_up()
        scoreboard.increase_level()
    loop_index += 1

screen.exitonclick()

import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_speed = 0.1

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(game_speed)

    # Detect successful crossing
    if player.is_at_finish_line() == True:
        game_speed *= 0.6
        scoreboard.increase_level()

    # Create and move cars
    dice = random.randint(1, 6)
    if dice == 1:
        car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    if car_manager.check_collision(player) == True:
        scoreboard.game_over()
        game_is_on = False
    screen.update()


screen.exitonclick()

import time
from turtle import Screen

from countdown import Countdown

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game, made with Python:")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
countdown = Countdown()

# Arrows
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# WASD or wasd
screen.onkeypress(snake.up, "W")
screen.onkeypress(snake.down, "S")
screen.onkeypress(snake.left, "A")
screen.onkeypress(snake.right, "D")

screen.onkeypress(snake.up, "w")
screen.onkeypress(snake.down, "s")
screen.onkeypress(snake.left, "a")
screen.onkeypress(snake.right, "d")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) <= 22:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with a wall:
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail:
    for segment in snake.segments:
        if segment != snake.head and snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

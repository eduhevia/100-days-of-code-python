import time
from tkinter import TclError
from turtle import Screen

from ball import Ball
from net import Net
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game, made with Python:")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()
net = Net()


screen.listen()

# Left paddle
screen.onkeypress(l_paddle.start_moving_up, "w")
screen.onkeyrelease(l_paddle.stop_moving_up, "w")
screen.onkeypress(l_paddle.start_moving_up, "W")
screen.onkeyrelease(l_paddle.stop_moving_up, "W")

screen.onkeypress(l_paddle.start_moving_down, "s")
screen.onkeyrelease(l_paddle.stop_moving_down, "s")
screen.onkeypress(l_paddle.start_moving_down, "S")
screen.onkeyrelease(l_paddle.stop_moving_down, "S")

# Right paddle
screen.onkeypress(r_paddle.start_moving_up, "Up")
screen.onkeyrelease(r_paddle.stop_moving_up, "Up")

screen.onkeypress(r_paddle.start_moving_down, "Down")
screen.onkeyrelease(r_paddle.stop_moving_down, "Down")

game_is_on = True

try:
    while game_is_on:
        time.sleep(ball.move_speed)

        l_paddle.update_position(ball.move_speed)
        r_paddle.update_position(ball.move_speed)

        l_paddle.update_position(ball.move_speed)
        r_paddle.update_position(ball.move_speed)

        screen.update()
        ball.move()

        # Detect collision with top and bottom walls
        if ball.ycor() > 279 or ball.ycor() < -279:
            ball.bounce_y()

        # Detect collision with right paddle
        if (
            (ball.xcor() > 320)
            and (ball.x_move > 0)
            and (ball.ycor() <= r_paddle.ycor() + 50)
            and (ball.ycor() >= r_paddle.ycor() - 50)
        ):
            ball.bounce_x()

        # Detect collision with left paddle
        if (
            (ball.xcor() < -320)
            and (ball.x_move < 0)
            and (ball.ycor() <= l_paddle.ycor() + 50)
            and (ball.ycor() >= l_paddle.ycor() - 50)
        ):
            ball.bounce_x()

        # Detect if right paddle misses
        if ball.xcor() > 385:
            ball.reset_position()
            scoreboard.l_point()
            if scoreboard.l_score == 10:
                scoreboard.declare_winner("Left Player")
                game_is_on = False

        # Detect if left paddle misses
        if ball.xcor() < -385:
            ball.reset_position()
            scoreboard.r_point()
            if scoreboard.r_score == 10:
                scoreboard.declare_winner("Right Player")
                screen.update()
                game_is_on = False

    screen.exitonclick()

except TclError:
    print("Game window was closed.")

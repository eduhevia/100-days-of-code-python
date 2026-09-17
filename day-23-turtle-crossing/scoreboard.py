import time
from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        self.highest_level = 0
        super().__init__()
        self.hideturtle()
        self.penup()
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1

        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
        time.sleep(1)

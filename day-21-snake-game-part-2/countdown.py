import time
from turtle import Screen, Turtle

ALIGNMENT = "center"
FONT = ("Courier", 30, "bold")


class Countdown(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 20)
        self.screen = Screen()

        self.start()

    def start(self):
        for i in range(3, 0, -1):
            self.clear()
            self.write(i, align=ALIGNMENT, font=FONT)
            self.screen.update()
            time.sleep(1)

        self.clear()
        self.write("GO!", align=ALIGNMENT, font=FONT)
        self.screen.update()
        time.sleep(0.5)

        self.clear()
        self.screen.update()

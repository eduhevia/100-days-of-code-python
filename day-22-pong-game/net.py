from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.pensize(5)
        self.goto(0, 300)
        self.setheading(270)
        self.draw_net()

    def draw_net(self):
        for _ in range(40):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(10)

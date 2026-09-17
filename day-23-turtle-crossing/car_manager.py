import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager(Turtle):
    def __init__(self):
        self.every_car = []

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.every_car.append(new_car)

    def check_collision(self, player):
        for car in self.every_car:
            if (
                abs(car.xcor() - player.xcor()) < 25
                and abs(car.ycor() - player.ycor()) < 20
            ):
                return True
        return False

    def move_car(self):
        for car in self.every_car:
            if car.xcor() < -320:
                car.hideturtle()
                self.every_car.remove(car)
            else:
                car.goto(car.xcor() - STARTING_MOVE_DISTANCE, car.ycor())

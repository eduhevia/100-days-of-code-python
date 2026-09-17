import random
from turtle import Screen, Turtle

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = -100
x = -230
all_turtles = []

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color("black", color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 35
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 225:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()

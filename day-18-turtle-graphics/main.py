import random
import turtle as t

screen = t.Screen()
screen.colormode(255)

tim = t.Turtle()
tim.speed("fastest")

colors = [
    (203, 171, 107),
    (152, 181, 196),
    (193, 161, 176),
    (151, 187, 174),
    (214, 204, 111),
    (207, 179, 198),
    (163, 202, 214),
    (174, 189, 213),
    (159, 214, 188),
    (113, 123, 186),
    (215, 180, 180),
    (181, 160, 66),
    (97, 97, 97),
    (99, 97, 98),
    (200, 206, 44),
    (129, 127, 128),
    (65, 63, 64),
    (101, 113, 153),
]

x = -225
y = -225


def draw_dot(x):
    random_color = random.choice(colors)
    tim.teleport(x, y)
    tim.dot(20, random_color)
    x += 50
    return x


for i in range(100):
    if i in range(10, 100, 10):
        x = -225
        y += 50
        x = draw_dot(x)

    else:
        x = draw_dot(x)


screen.exitonclick()

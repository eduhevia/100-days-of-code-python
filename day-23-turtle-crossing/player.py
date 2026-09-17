from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
START_ORIENTATION = 90  # Facing North


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(START_ORIENTATION)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_y)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

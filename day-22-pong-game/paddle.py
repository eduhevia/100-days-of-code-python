from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()

        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.moving_up = False
        self.moving_down = False

    def go_up(self, ball_speed):
        distance = 175 * ball_speed
        new_y = self.ycor() + distance
        if new_y < 250:
            self.goto(self.xcor(), new_y)

    def go_down(self, ball_speed):
        distance = 175 * ball_speed
        new_y = self.ycor() - distance
        if new_y > -250:
            self.goto(self.xcor(), new_y)

    def start_moving_up(self):
        self.moving_up = True

    def stop_moving_up(self):
        self.moving_up = False

    def start_moving_down(self):
        self.moving_down = True

    def stop_moving_down(self):
        self.moving_down = False

    def update_position(self, ball_speed):
        if self.moving_up:
            self.go_up(ball_speed)
        if self.moving_down:
            self.go_down(ball_speed)

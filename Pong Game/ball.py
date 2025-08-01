from turtle import Turtle

class Ball(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(start_pos)
        self.x_velocity = 10
        self.y_velocity = 10
        self.move_speed=.1

    def move(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_velocity *= -1

    def bounce_x(self):
        self.x_velocity *= -1
        self.move_speed *=.9
    def reset_pos(self):
        self.goto(0,0)


import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def rand(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        return(rand_x,rand_y)
    def refresh(self):
        self.goto(self.rand())





import random
from turtle import Turtle

class Food(Turtle):
    
    @staticmethod
    def random_color():
        color_codes = "abcdef0123456789"
        hex = "#"
        for i in range(6):
            hex+=random.choice(color_codes)
        return hex

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("turtle")
        self.shapesize(0.8, 0.8)
    
    def create_food(self):
        self.color(self.random_color())
        x = random.randint(-600, 600)
        y = random.randint(-335, 335)
        self.goto(x,y)

import time
from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.snake_cells = []
        self.head_position = (0,0)
        self.window = Screen()
        self.window.bgcolor("black")

    def create_snake(self):
        x = y = 0
        self.window.tracer(0)
        for i in range(3):
            self.add_cell(x,y)
            x-=20
        self.window.update()

    def add_cell(self, x, y):
        body = Turtle(shape="square")
        body.color("white")
        body.shapesize(0.8,0.8)
        body.penup()
        body.goto(x, y)
        self.snake_cells.append(body)

    def move(self, speed=0.5):
        self.window.tracer(0)
        
        position = self.snake_cells[0].pos()
        self.snake_cells[0].forward(20)
        for cell in self.snake_cells[1:]:
            old_position = cell.pos()
            cell.goto(position)
            position = old_position
        time.sleep(speed)
        self.window.update()

    def up(self):
        if int(self.snake_cells[0].heading())!=270:
            self.snake_cells[0].setheading(90)

    def down(self):
        if int(self.snake_cells[0].heading())!=90:
            self.snake_cells[0].setheading(270)

    def right(self):
        if int(self.snake_cells[0].heading())!=180:
            self.snake_cells[0].setheading(0)

    def left(self):
        if int(self.snake_cells[0].heading())!=0:
            self.snake_cells[0].setheading(180)

    def start(self):
        self.window.listen()
        self.window.onkeypress(self.move)
        self.window.onkeypress(self.up, "w")
        self.window.onkeypress(self.down, "s")
        self.window.onkeypress(self.right, "d")
        self.window.onkeypress(self.left, "a")  
  
    def click_exit(self):
        self.window.exitonclick()

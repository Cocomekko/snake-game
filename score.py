from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,320)
        self.show_score()
    
    def update_score(self):
        self.score+=1

    def show_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 20, "normal"))

    def over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"GAME OVER", False, align="center", font=("Arial", 25, "normal"))

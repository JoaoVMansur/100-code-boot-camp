from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        
    
    
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.line()
    
    
    
    def l_point(self):
        self.l_score +=1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
    
    def line(self):
        self.goto(0, -300)
        self.pendown()
        self.setheading(90)
        self.pensize(3)
        for dashes in range(30):

            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
        self.penup()
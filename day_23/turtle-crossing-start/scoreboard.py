from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.lvl}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.lvl}", align="left", font=FONT)
    
    def pass_lvl(self):
        self.lvl +=1
    
    def game_over(self):
        
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
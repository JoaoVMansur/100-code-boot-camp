from turtle import Turtle
ALIGMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("day 20_21/data.txt", mode="r") as file:

            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day 20_21/data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()

    
    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} Highest score: {self.high_score}", False, align=ALIGMENT, font=FONT)
    
    
    
    def increase_score(self):
        self.score +=1
        self.update_score()
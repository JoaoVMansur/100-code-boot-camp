from turtle import Turtle, Screen
import random as r

is_rece_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt=" Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_x = -225
start_y = -125

list_turtles = []


for turtle_index in range(0, 6):

    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(start_x, start_y)
    start_y +=45
    list_turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in list_turtles:
        if turtles.xcor() >230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            break
        turtles.pendown()
        
        move = r.randint(0, 20)
        turtles.forward(move)




screen.exitonclick()


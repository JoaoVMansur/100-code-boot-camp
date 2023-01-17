import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
tim.color("white")
tim.hideturtle()
tim.penup()
tim.goto(0, -300)
tim.pendown()
tim.setheading(90)
tim.pensize(5)
for dashes in range(30):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen.update()


screen.exitonclick()
import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "black"]

tim.speed(0)

def draw_graph(size_of_gap):

    for _ in range(int(360/size_of_gap)):

        tim.color(random.choice(colours))
        tim.setheading(tim.heading()+size_of_gap)
        tim.circle(100)

    


draw_graph(1)

screen = t.Screen()
screen.exitonclick()
import turtle as t
import random

tim = t.Turtle()
tim.penup()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.speed(0)
x = -225 
y = -100
def initial_position(x, y):
    
    tim.setx(x)
    tim.sety(y)
    

def change_position():
    global y
    y+= 40
    tim.setx(x)
    tim.sety(y)
    


def paint_dots(size):
    for _ in range(size):
        tim.dot(20, (random.choice(colours)))
        
        tim.forward(50)
        
        


initial_position(x, y)
size = int(input("what size of the art do you want?: "))
for times in range(size):
    paint_dots(size)
    change_position()




screen = t.Screen()
screen.exitonclick()
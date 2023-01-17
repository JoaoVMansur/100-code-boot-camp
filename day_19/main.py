import turtle as t
tim = t.Turtle()
screen = t.Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.bk(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.lt(10)
def clear():
    tim.clear()
    tim.penup()
    tim.setx(0)
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeypress(key="c", fun=clear)
screen.exitonclick()
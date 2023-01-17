from turtle import Turtle, Screen
from paddle_class import Paddle
from ball_class import Ball
from score_class import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle(360)
l_paddle = Paddle(-360)
screen.update()
ball = Ball(0)



screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
score = Scoreboard()
score.line()
 
game_is_on = True 
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect R paddle misses
    if ball.xcor() > 385:
        ball.refresh()
        score.line()
        score.l_point()
        
    #Detect L paddle misses

    if ball.xcor() < -385:
        ball.refresh()
        score.line()
        score.r_point()
        
    
    
    #Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce("up")
        
    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce("right")
        ball.move_speed *= 0.9







screen.exitonclick()
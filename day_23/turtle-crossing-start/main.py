import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkeypress(player.move, "Up")
carro = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    carro.create_car()
    carro.move()
    screen.update()
    #Detec colision with car
    for cars in carro.cars:
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False

    
    #Detec if player reached the other side 
    if player.ycor() > 280:
        player.restart_lvl()
        carro.lvl_up( )
        score.pass_lvl()
        score.update_score()
screen.exitonclick()
import time
from turtle import Screen
from player import Player
from cars import CarManager
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


score = Scoreboard()
car=CarManager()
player = Player()
def move():
    if(player.ycor() < 280):
        player.forward(10)
screen.listen()
screen.onkey(move,"Up")
screen.update()
game_is_on = True


while game_is_on:
    time.sleep(0.1)
    car.move()
    car.newcar()
    for carr in car.allcars:
        if(player.distance(carr.pos()) < 20):
            score.gameover()
    if(player.ycor() >= 275):
        player.newlevel()
        car.faster()
        score.nextlevel()
        car.newcar()
    screen.update()

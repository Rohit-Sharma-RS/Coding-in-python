import time
import turtle
from turtle import Turtle,Screen
from computer import Player
from ball import Ball
import time
from score import Score

game_on = True

screen = Screen()
screen.title("PONG GAME")
screen.setup(width = 550,height = 550)
screen.bgcolor("black")
screen.tracer(0)

player = Player((250,0))
player2 = Player((-250,0))

ball=Ball()



screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player2.up, "w")
screen.onkey(player2.down, "s")


score=Score()
while(game_on):

    time.sleep(ball.move_speed)
    ball.move()
    if(ball.ycor() >= 250 or ball.ycor() <=-250):
        ball.bounce_y()
    if(ball.distance(player.pos()) < 55 and ball.xcor() > 235):
        ball.bounce_x()
        score.rscore += 1
        score.update()
    if(ball.distance(player2.pos()) < 55 and ball.xcor() < -235):
        ball.bounce_x()
        score.lscore += 1
        score.update()
    screen.update()

    if(ball.xcor() > 250 or ball.xcor() < -250):
        ball.reset_position()

screen.exitonclick()
turtle.done


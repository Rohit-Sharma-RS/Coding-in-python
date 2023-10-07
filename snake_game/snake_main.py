from snake import Snake
from turtle import Turtle,Screen
import time
from food import Food
from scoreboard import Scoreboard


game_on=True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake game")
screen.tracer(0)

score = 0
snake=Snake()
food=Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



while (game_on):
    time.sleep(0.1)
    snake.move()
    screen.update()
    #detect food
    if(snake.segment[0].distance(food) < 15):
        food.ref()
        scoreboard.increase_score()
        snake.grow()


    #detect collison with wall
    if(snake.segment[0].xcor() > 290 or snake.segment[0].xcor() < -290 or snake.segment[0].ycor() < -290
            or snake.segment[0].ycor() > 290):
        scoreboard.game_over()
        game_on=False




    #detect collison with snake
    for i in range(2,len(snake.segment)):
        if(snake.head.distance(snake.segment[i]) < 10):
            scoreboard.game_over()
            game_on=False
            
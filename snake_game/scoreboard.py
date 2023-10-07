from turtle import Turtle, done, Screen
import time
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(0, 240)
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
        self.screen = Screen()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 240)
        self.write(f"Score: {self.score}", True, align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !", True, align="center", font=("Arial", 24, "normal"))
        self.goto(0,-40)
        self.write("Press space to exit", True, align="center", font=("Arial", 24, "normal"))
        done()




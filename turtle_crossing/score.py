from turtle import Turtle,Screen,done
import time


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-140,240)
        self.write(f"level: {self.level} ",align="center",font=FONT)
        self.hideturtle()


    def nextlevel(self):
        time.sleep(0.5)
        self.level += 1
        self.clear()
        self.goto(-140,240)
        self.write(f"level: {self.level} ", align="center", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
        done()





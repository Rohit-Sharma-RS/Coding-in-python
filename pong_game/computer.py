from turtle import Turtle
POSITION2=[(240,0),(240,20),(240,-20)]
segment=[]
class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if (self.ycor() < 220):
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def down(self):
        if (self.ycor() > -220):
            y = self.ycor() - 20
            self.goto(self.xcor(), y)


from turtle import Turtle,Screen


class Player(Turtle):
    def __init__(self):
        super.__init__
        self.player = Turtle("square")
        self.player.color("white")
        self.player.shapesize(stretch_wid=5, stretch_len=1)
        self.player.penup()
        self.player.goto(-250, 0)


    def up(self):
        y=self.player.ycor()+20
        self.player.goto(-250,y)

    def down(self):
        y=self.player.ycor()-20
        self.player.goto(-250,y)




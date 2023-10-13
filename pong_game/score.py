from turtle import Turtle,Screen



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.curr_score=0
        self.hideturtle()
        self.rscore = 0
        self.lscore = 0
        self.hideturtle()
        self.goto(-100,150)
        self.write(self.lscore, align="center", font=("Arial",80,"normal"))
        self.goto(100,150)
        self.write(self.rscore, align="center", font=("Arial",80,"normal"))

    def update(self):
        self.clear()
        self.goto(-100, 150)
        self.write(self.lscore, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 150)
        self.write(self.rscore, align="center", font=("Arial", 80, "normal"))



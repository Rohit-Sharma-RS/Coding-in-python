from turtle import Turtle, Screen
import time


MOVEDISTANCE = 20
POSITION = [(0, 0), (-20, 0), (-40, 0)]

class Snake():
    def __init__(self):
        self.segment = []
        self.createsnake()
        self.head=self.segment[0]
        self.length = 3

    def createsnake(self):
        for i in POSITION:
            self.addsnake(i)


    def addsnake(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segment.append(tim)

    # very amazing to turn the snake left you could use this logic
    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            newx = self.segment[i - 1].xcor()
            newy = self.segment[i - 1].ycor()
            self.segment[i].goto(newx, newy)
            # most noteworthy logic I learned from this project
            # helps all pieces of the snake to follow the first piece everywhere it goes
        self.segment[0].forward(MOVEDISTANCE)


    def up(self):
        #to move up we set the head of the snake to move 90 degrees of the screen i.e. North
        self.segment[0].setheading(90)


    def down(self):
        self.segment[0].setheading(270)


    def left(self):
        self.segment[0].setheading(180)

    def right(self):
        self.segment[0].setheading(0)

    def grow(self):
        self.addsnake(self.segment[-1].position())

    def reset(self):
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.createsnake()
        self.head = self.segment[0]



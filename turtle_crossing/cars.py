from turtle import Turtle
import random
import time


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        #we collect all turtles in a list of cars which we move later !
        self.allcars = []
        self.speed = 10
    def newcar(self):
        #the best takeaway from this project
        #to decrease the frequency of cars we used probability.
        #hence a car appears once every 5 times which produces a good frequency according to me
        randomchoice = random.randint(1,5)
        if(randomchoice == 3):
            car=Turtle()
            car.shapesize(stretch_wid = 1, stretch_len = 2)
            car.color(random.choices(COLORS))
            newx = 280
            car.shape("square")
            car.penup()
            car.goto(x = newx, y = random.randint(-200, 200))
            self.allcars.append(car)


    def move(self):
        for car in self.allcars:
            car.backward(self.speed)

    def faster(self):
        self.speed += 5


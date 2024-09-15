import turtle

#timmy is an object created from class Turtle
timmy=turtle.Turtle()
print(timmy)
#method shape changes shape of timmy
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(200)
print(timmy.position())


#screen() is also a class
myscreen=turtle.Screen()
print(myscreen.canvheight)
#now we have an attribute associated with my screen object attribute is basic data


#now we have methods or functions
#we have functions within class called methods just use () to signify that
myscreen.exitonclick()
#this fucntion shows screen forever until clicked
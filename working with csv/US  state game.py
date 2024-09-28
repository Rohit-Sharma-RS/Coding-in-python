import turtle
import pandas as pd

l=[]
answered = []
chances = 5
screen = turtle.Screen()
screen.title("U.S. State game")
data = pd.read_csv("50_states.csv")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-200,0)

for state in data.state:
    l.append(state)
while chances > 0 and len(answered)<=50:

    p = turtle.textinput(f"{len(answered)}/50 guessed correctly", f"Please guess a state (You have {chances} guesses)")
    p = p.title()
    if(p=="Exit"):
        break

    if p in l and p not in answered:
        mystate = data[data.state==p]
        writer.penup()
        writer.goto(int(mystate.x), int(mystate.y))
        writer.write(mystate.state.item())
        answered.append(p)

    elif p in answered:
        print("That's already guessed")
    else:
        chances -= 1
if(chances == 0):
    screen.bye()

d={"State":[]}
for state in data.state:
    if(state not in d["State"] and state not in answered):
        d["State"].append(state)


d = pd.DataFrame(d)
d.to_csv("Missing states")
import pandas as pd

data =  pd.read_csv("squirrel.csv")
g,r,b,n = 0,0,0,0
for i in (data["Primary Fur Color"]):
    if(i == "Gray"):
        g += 1
    elif(i == "Cinnamon"):
        r += 1
    elif(i == "Black"):
        b += 1
    else:
        n += 1


new = {"Color": ["Gray", "Black", "Red"], "Count": [g,b,r]}

new = pd.DataFrame(new)
new = new.to_csv("new.csv")
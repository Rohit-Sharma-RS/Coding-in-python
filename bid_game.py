#a private bidding game with an art piece!
import os
def clear():
    os.system('cls')
import art
repeat=True
d={}
ls=[]
while repeat==True:
    clear()
    print(art.logo)
    name=input("what is your name ")
    bid=int(input("what is your bid "))
    d[name]=bid
    n=input("are there any other bidders type yes or no ")
    if n != "yes":
        repeat="False"
max = -1
for names in d:
    if d[names]>max:
        max=d[names]
        max_bidder=names
        
print(f"The winner is {max_bidder} with a bid of {max}")

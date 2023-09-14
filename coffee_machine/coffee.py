from logo import logo
import os
def clear():
    os.system('cls')
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
i=int(input('Welcome \nenter 1 to continue '))


def report():
    print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}")


def r_check():
    if(MENU[d]["ingredients"]["water"]>resources["water"]):
        print("Sorry not enough water")
        clear()
    elif(MENU[d]["ingredients"]["milk"]>resources["milk"]):
        print("Sorry not enough milk")
        clear()
    elif(MENU[d]["ingredients"]["coffee"]>resources["coffee"]):
        print("Sorry not enough coffee")
        clear()
    else:
        return 1


while(i==1):
    clear()
    print(logo)
    d = input("What would you like to have?\n1. espresso\n2. latte\n3. cappuccino\n4. EXIT\n").lower()
    if(d=='exit'):
        exit()
    if (d in MENU) and (r_check()):
        bill =float(MENU[d]['cost'])
        print("Your total came out at ", bill)
        c = float(input("Please insert coins "))
        if (c<bill):
            print("That's not enough money\nMoney refunded")

        else:
            print(f"Here is your {d} ☕ enjoy!!")
            resources["water"]=resources["water"]-MENU[d]["ingredients"]["water"]
            resources["milk"]=resources["milk"]-MENU[d]["ingredients"]["milk"]
            resources["coffee"]=resources["coffee"]-MENU[d]["ingredients"]["coffee"]
            left=round(c-bill,2)

            if(not(left==0)):
                print("Here is your change ",left)


    elif(d=='report'):
        report()

    else:
        print("Wrong input ")

    i=int(input("Want more? Enter 1 to continue. "))


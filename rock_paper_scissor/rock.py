import random
import os
import art
def clear():
    os.system('cls')
l=[1,2,3]
def choosing():
    return(random.choice(l))

def start_game():
    print(art)
    n=input("Do you wanna play a game of rock paper and scissors\npress 'y' if you wanna else 'n'\n ").lower()
    clear()
    while(n=='y'):
        if(n=='y'):
            comp_choice=choosing()
            d={1:"rock",2:"paper",3:"scissors"}
            player_choice=int(input("enter 1 for rock\nenter 2 for paper\nenter 3 for scissors\n"))
            print(f'you chose {d[player_choice]} and the computer chose {d[comp_choice]}')
            if(player_choice==comp_choice):
                print("It is a draw")
            elif(player_choice==comp_choice+1 and not(comp_choice==3)):
                print("You win")
            elif((player_choice==3 and comp_choice==1) or (comp_choice==player_choice+1 and not(player_choice==3))):
                print("You lose")
            else:
                print("You win")
            n=input("Do you wanna play a game of rock paper and scissors\n press 'y' if you wanna else 'n' ").lower()
        elif(n=='n'):
            clear()
            exit()
        else:
            print("Invalid choice")
start_game()
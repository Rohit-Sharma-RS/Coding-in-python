BACKGROUND_COLOR = "#B1DDC6"

import pandas as pd
from tkinter import *
import random
import time


#------------The words and words changing on clicking buttons------------#
dict_data = pd.read_csv("french_words.csv")
dict_data =dict_data.to_dict(orient="records")


first_word = random.choice(dict_data)
current_card = first_word
french_word = first_word['French']


#-------button commands------#
def change_word():
    global current_card, rotation
    screen.after_cancel(rotation)
    current_card = random.choice(dict_data)
    canvas.itemconfig(creator, image=front)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(id, text=current_card['French'])
    rotation = screen.after(3000, rotate)


def changeknownword():
    global current_card
    dict_data.remove(current_card)
    with open("unlearned_words.csv",'w') as f:
        f.writelines(str(dict_data))
    change_word()


#-------------Rotating the flashcard-----------#
def rotate():
    canvas.itemconfig(id, text=current_card["English"])
    canvas.itemconfig(creator,image=back)
    canvas.itemconfig(title, text="English")


#---------The UI----------#
screen = Tk()
screen.title("Flashy Flash card app")
screen.config(padx=20,pady=20,bg=BACKGROUND_COLOR)


rotation = screen.after(3000, rotate)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)
front=PhotoImage(file="card_front.png")
back = PhotoImage(file="card_back.png")
creator = canvas.create_image(400,263, image=front)
title=canvas.create_text(400,160, text="French", font=("Arial", 20, "italic"))
id = canvas.create_text(400,263, text=french_word, font=("Arial", 40, "bold"))
canvas.grid(row=0,column=0,columnspan=3)


tick = PhotoImage(file="right.png")
tick_button = Button(image=tick, highlightthickness=0, command=changeknownword)
tick_button.grid(row= 1, column=2)


cross = PhotoImage(file="wrong.png")
cross_button = Button(image=cross, highlightthickness=0, command=change_word)
cross_button.grid(row=1, column=0)


screen.mainloop()


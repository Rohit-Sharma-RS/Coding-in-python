from tkinter import *
from tkinter import messagebox
import pandas
import pandas as pd

#--------------Random Password generator----------
import random
def randompass():
    pass_entry.delete(0,END)
    finalpass = ' '
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    randompass=[]
    let = [randompass.append(random.choice(letters)) for _ in range(random.randint(8,10))]
    num = [randompass.append(random.choice(numbers)) for _ in range(random.randint(2,4))]
    sym = [randompass.append(random.choice(symbols)) for _ in range(random.randint(2,4))]
    for i in randompass:
        finalpass += i
    pass_entry.insert(END,finalpass)

#---------------Saving data to file----------------
def add_function():

    if(pass_entry.get()==''or web_entry.get()=='' or email_entry.get()==''):
        messagebox.showwarning(title="Attention", message="Don't leave any field empty")
    else:
        if (messagebox.askokcancel(title="Attention", message="Is It ok to save?")):
            f = open("data.txt", "a")
            f.write(f"{web_entry.get()} | E-mail:{email_entry.get()} | Password : {pass_entry.get()} \n")
            pass_entry.delete(0, END)
            web_entry.delete(0, END)
            f.close()


screen = Tk()
screen.minsize(240,240)
screen.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
v = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=v)
canvas.grid(row=0,column=1)

website = Label(text="Website :")
website.config(padx=10, pady=10)
website.grid(row=1,column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)

email = Label(text="E-mail :  " )
email.config(padx=10, pady=10)
email.grid(row=2,column=0)

email_entry=Entry(width=35)
email_entry.insert(END, "vampire.instinct777@gmail.com ")
email_entry.grid(row=2,column=1,columnspan=2)

password = Label(text="Password :")
password.config(padx=10, pady=10)
password.grid(row=3,column=0)

pass_entry = Entry(width=35)
pass_entry.grid(row=3,column=1, columnspan=2)

generate = Button(text="Generate Password", width=14, command=randompass)
generate.grid(row=3,column=3)



add=Button(text="Add", width=36, command=add_function)

add.grid(column=1,row=4, columnspan=2)


screen.mainloop()

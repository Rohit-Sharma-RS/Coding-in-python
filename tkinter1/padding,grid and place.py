from tkinter import *

window = Tk()
window.config(padx=100, pady=200)

window.title("Grid demo")
window.minsize(500,500)

label=Label(text="Hello there")
label.grid(column=1,row=1)
label.config(padx=50, pady=50)#add paddings so there is some space

button=Button(text="Click here")
button.grid(column=0, row=0)#forms a grid and places text accordingly

text=Text(width=20, height=15)
text.insert(END, "Already written text")
text.place(x=100,y=100)#places at a point




window.mainloop()
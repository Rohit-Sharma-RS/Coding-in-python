from tkinter import *

screen = Tk()
screen.minsize(250,250)
screen.title("Miles to Kms converter")
screen.config(padx=100, pady=100)

#entry for the function...
entry1 = Label(text="is equal to")
entry1.grid(column=0,row=1)
entry1.config(padx=10,pady=10)


#label for input in miles
miles = Entry(width=20)
miles.grid(column=1, row=0)
miles.focus()

#label for output in kms
km = Entry(text="KMs")
km.grid(column=1, row=1)


def doaction():
    km.insert(END,f"{int(miles.get())*100}")



#button for conversion
button = Button(text="Convert", command=doaction)
button.grid(row=2, column=1)

#2 more labels
label2 = Label(text="Miles")
label2.grid(column=2, row=0)

label3 = Label(text="KMs")
label3.grid(column=2, row=1)


screen.mainloop()
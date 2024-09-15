from tkinter import *

#screen
screen=Tk()
screen.title("This Demonstrates all the function of tkinter")
screen.minsize(width=500,height=500)

#Label
label = Label(text="This is a Label",font=("ALgerian",20,"bold"))
label.pack()


def doaction():
    label.config(text="Button Clicked Label text changed")

def change():
    label.config(text=entry.get())

#Button
button = Button(text="This is a button... click it", command=doaction )
button.pack()

#Entry
entry = Entry(width=40)
entry.insert(END,"This is an entry type something here")
entry_data = entry.get()
entry.pack()

#demonstrating a use of entry
Entrybutton = Button(text="After entry click this", command = change)
Entrybutton.pack()

#Textbox
text = Text(height = 5, width=30)
text.focus()#put cursor inside text box
text.insert(END,chars="This is the textbox, Some text to begin with")

print(text.get("1.3",END))#get text from the first line and 3rd character
text.pack()


def spinboxused():
    print(spinbox.get())
#SpinBox
spinbox = Spinbox(from_=0, to=100, width=5, command=spinboxused)
spinbox.pack()

#scale is kinda different as it has its own value and hence the value gets passed to function automatically
def scaleused(value):
    print(value)
#Scale
scale = Scale(from_=0,to=10,command=scaleused)
scale.pack()

def checkbuttonused():
    print(checked_state.get())
#Check-button
checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbuttonused)
#check button has an additional variable section
#checked state is the most important point here
checkbutton.pack()



def radio_used ():
    print(radio_state.get())
#RadioButton
radio_state = IntVar()
radiobutton = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command=radio_used)
radiobutton.pack()
radiobutton2.pack()



def listbox_used(event):
    print(listbox.get(listbox.curselection()))
#listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Orange", "Banana", "Cherry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

#this loop shall run forever
screen.mainloop()
# def calculate(**kwargs):
#     n=0
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n
#
# print(calculate(add=4, multiply = 9))

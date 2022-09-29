from faulthandler import disable
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root,text = "I clicked a Button")
    myLabel.pack()

myButton = Button(root,text = 'Click Me!',padx = 50,command = myClick,fg = 'blue',bg = 'red')

myButton.pack()

root.mainloop()
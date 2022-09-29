from tkinter import *

root = Tk()

e = Entry(root,width = 50,bg = '#fff',fg = '#000',borderwidth = '5')
e.insert(0,"Enter your name: ")
e.pack()

def myClick():
    myLabel = Label(root,text = e.get())
    myLabel.pack()

myButton = Button(root,text = 'Enter your name',padx = 50,command = myClick,fg = 'black',bg = '#fff')
myButton.pack()

root.mainloop()
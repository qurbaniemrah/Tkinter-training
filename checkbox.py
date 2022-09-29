from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("New Window")
root.geometry("400x400")

def show():
    myLabel = Label(root, text = var.get()).pack()



var = StringVar()

c = Checkbutton(root,text = "Check this box, I dare you!", variable=var,onvalue="Pizza", offvalue="Hamburger")

c.pack()



myButton = Button(root,text = "Show Selection", command = show).pack()



root.mainloop()
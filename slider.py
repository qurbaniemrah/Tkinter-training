from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("New Window")
root.geometry("400x400")
# root.resizable(False,False)

vertical  = Scale(root,from_ = 0, to = 200)
vertical.pack()

horizontal  = Scale(root,from_ = 0, to = 200, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()

def slide():
    my_label = Label(root, text = horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

my_btn = Button(root, text = "Click Me!", command=slide).pack()    



root.mainloop()
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("New Window")

def open():
    global my_img
    top = Toplevel()
    top.title("My second window")
    my_img = ImageTk.PhotoImage(Image.open("images/2.png"))
    my_label = Label(top, image = my_img).pack()
    btn2 = Button(top,text = "Close window",command = top.destroy).pack()



btn = Button(root, text = "Open Second Window", command = open).pack()


mainloop()
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title("Messages Box")


def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
    Label(root, text = response).pack()




Button(root, text = 'Popup', command=popup).pack()








mainloop()
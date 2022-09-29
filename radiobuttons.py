from ast import Lambda
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio button")

# r = IntVar()
# r.set("2")

TOPPINGS = [
    ("Paperoni","Paperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Paperoni")

for text,topping in TOPPINGS:
    
    Radiobutton(root,text = text, variable=pizza, value = topping).pack(anchor = W)





def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


Radiobutton(root, text="Option 1", variable=pizza, value=1,
            command=lambda: clicked(pizza.get())).pack()
Radiobutton(root, text="Option 2", variable=pizza, value=2,
            command=lambda: clicked(pizza.get())).pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

# myButton = Button(root, text = "Clicked Me!", command = Lambda: clicked(pizza.get()))
# myButton.pack()


mainloop()

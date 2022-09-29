from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Images viewer')


my_img1 = ImageTk.PhotoImage(Image.open("images/1.png"))

my_img2 = ImageTk.PhotoImage(Image.open("images/2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.png"))

image_list = [my_img1,my_img2,my_img3,my_img4]


my_label = Label(image = my_img1)




button_back = Button(root,text = "<<")

button_exit = Button(root,text = "EXIT PROGRAM", command = root.quit)
button_forward = Button(root,text=">>")

button_back.grid(row=2,column=0)
button_exit.grid(row = 2,column=1)
button_forward.grid(row=2, column=2)



root.mainloop()
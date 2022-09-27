import tkinter as tk

form = tk.Tk()
form.title =('Tkinter dersleri-3')
form.geometry('500x250+500+200')
form.minsize(450,400)
form.maxsize(550,550)
form.resizable(False,False)
label = tk.Label(form,text='Ders-3')
label.pack()

form.mainloop()
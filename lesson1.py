import tkinter as tk

form = tk.Tk()
form.title('Tkinter dersleri-1')
etiket = tk.Label(text='Tkinter Python')
etiket.pack() #ekrana dusmesi ucun yazilir
etiket2 = tk.Label(form,text = 'Python Tkinter Dersleri')
etiket2.pack()
form.mainloop()

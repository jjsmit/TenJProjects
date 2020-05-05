from tkinter import *
from tkinter import ttk
##from Tkinter import *
from tkinter.messagebox import *
import tkinter.messagebox



window = Tk()
window.title("J2T Chat")
message = Text(window)
message.pack()

input_user = StringVar()
input_field = Entry(window, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

def Enter_pressed(event):
    input_get = input_field.get()
    print(input_get)
    message.insert(INSERT, ' typed message: %s\n' %input_get)
    input_user.set('')
    return "berak"

frame = Frame(window)
input_field.bind("<Return>", Enter_pressed)
frame.pack()


window.mainloop()

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter.messagebox


def show_answer():
    Ans = num1.get()
    tkinter.messagebox.showinf('message',Ans)

root = Tk()

root.title("First Window")
##ttk.Button(root, text = "Hello").grid()
frame = Frame(root)

Label(root, text="Enter Num 1:").grid(row=0)
Label(root, text = "Response").grid(row=2)
num1 = Entry(root)
blank = Entry(root)
Button(root,text='Show',command=show_answer).grid(row=4,column=1,sticky=W,pady=4)
num1.grid(row=0, column=1)
blank.grid(row=2, column=1)


##labelText = StringVar()
##label = Label(frame, textvariable=labelText)
##
##
##button = Button(frame, text="Click Me")
##labelText.set("label 1")
##
##label.pack()
##button.pack()
##frame.pack()


root.mainloop()

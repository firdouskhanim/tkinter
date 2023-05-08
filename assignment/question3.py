from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("300x170")

topheader=Frame(win)
topheader.place(x=10,y=0)

label=Label(topheader,text="This is Label Frame",fg="blue")
label.pack()

T = Text(win, height = 5, width = 52)
l = Label(win, text = "1. This is a Label.")
l.place(x=10,y=30)

l = Label(win, text = "2.This is another Label.")
l.place(x=10,y=60)

l = Label(win, text = """3. We can add multiple
widgets in it.""")
l.place(x=10,y=90)

win.mainloop()
import tkinter as tk
from tkinter import*
from tkinter import ttk


win = tk.Tk()
win.geometry("400x250")

topheader=Frame(win)
topheader.pack()
label=Label(topheader,text="FOOD ITEMS",font= 10)
label.pack()

listbox = tk.Listbox(win,bg="grey",fg="yellow",height=15,width=20,font=10)


listbox.insert(0, "Nachos")
listbox.insert(1, "Sandwich")
listbox.insert(2, "Burger")
listbox.insert(3, "Pizza")
listbox.insert(4, "Burrito")


listbox.place(x=100,y=30)
win.mainloop()
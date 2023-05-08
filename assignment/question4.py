import tkinter as tk
from tkinter import*
from tkinter import ttk


win = tk.Tk()
win.title("Vinayak App")
win.geometry("300x170")

topheader=Frame(win)
topheader.place(x=5,y=5)
label=Label(topheader,text="Choose the the week day here",font=("Arial", 10))
label.pack()



options = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
selected_option = tk.StringVar()
selected_option.set(options[0])
option_menu = tk.OptionMenu(win, selected_option, *options, command=lambda x: print(f"Selected: {selected_option.get()}"))
option_menu.config(width=12, bg="green", fg="white",font=("Helvetica", 12, "italic"),activebackground="white")
option_menu.place(x=60,y=40)

win.mainloop()


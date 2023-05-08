from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("300x170")

topheader=Frame(win)
topheader.place(x=10,y=0)

label=Label(topheader,text="This is Label Frame",fg="blue")
label.pack()
b1_button = Button(win, text ="Button 1")
b1_button.place( x=40,y=30)

b1_button = Button(win, text ="Button 2")
b1_button.place( x=150,y=30)


checkbtn1=StringVar()
checkbtn2=StringVar()

select=Checkbutton(win,text='Checkbutton 1',variable=checkbtn1)
select.place(x=20,y=70)

select=Checkbutton(win,text='Checkbutton 2',variable=checkbtn2)
select.place(x=20,y=100)

win.mainloop()
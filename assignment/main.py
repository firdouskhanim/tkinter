from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("300x170")


T = Text(win)

l = Label(win, text = "Select Programming language of your choice ",font=("Arial", 10))
l.place(x=20,y=20) 


checkbtn1=StringVar()
checkbtn2=StringVar()
checkbtn3=StringVar()
checkbtn4=StringVar()

select=Checkbutton(win,text='Java',variable=checkbtn1)
select.place(x=20,y=40)

select=Checkbutton(win,text='C++',variable=checkbtn2)
select.place(x=20,y=60)

select=Checkbutton(win,text='Python',variable=checkbtn3)
select.place(x=20,y=80)

select=Checkbutton(win,text='C',variable=checkbtn4)
select.place(x=20,y=100)

win.mainloop()
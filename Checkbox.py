from tkinter import *
top = Tk()
top.geometry("400x250")

uname = Label(top, text="User Name:").place(x=40, y=50)
password = Label(top, text="Password:").place(x=40, y=90)

e1 = Entry(top)
e1.place(x=110, y=50)
e2 = Entry(top)
e2.place(x=110, y=90)

var1 = IntVar()
var2 = IntVar()
Checkbutton(top, text='Male', variable=var1).place(x=40, y=130)
Checkbutton(top, text='Female', variable=var2).place(x=40, y=160)
top.mainloop()
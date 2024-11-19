from tkinter import*
top = Tk()
top.geometry("400x250")

uname = Label(top, text="User Name:").place(x=40, y=50)
password = Label(top, text="Password:").place(x=40, y=90)
e1 = Entry(top)
e1.place(x=110, y=50)
e2 = Entry(top,show="*")
e2.place(x=110, y=90)
gender = IntVar()

Radiobutton(top, text='Male', variable=gender,value=1).place(x=40, y=130)
Radiobutton(top, text='Female', variable=gender,value=2).place(x=40, y=160)

top.mainloop()

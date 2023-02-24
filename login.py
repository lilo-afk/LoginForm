from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.title('Sign in')
frame.geometry('950x500+300+200')
frame.configure(bg="#eee")
frame.resizable(False,False)

img = PhotoImage(file='./img/login.png')
Label(frame,image=img,bg='#eee').place(x=50, y=40)

frame.mainloop()
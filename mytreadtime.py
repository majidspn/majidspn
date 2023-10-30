from tkinter import*
from threading import Thread
from tkinter import messagebox
import time

def timer1():
    s=int(e1.get())
    while s>=0:
        lb1.config(text=str(s))
        time.sleep(1)
        s-=1
    messagebox.showinfo("alarm","timer1 complete")
def timer2():
    s=int(e2.get())
    while s>=0:
        lb2.config(text=str(s))
        time.sleep(1)
        s-=1     
    messagebox.showinfo("alarm","timer1 complete")
def py1():
    p1=Thread(target=timer1)
    p1.start()

def py2():
    p2=Thread(target=timer2)
    p2.start()

root=Tk()
root.geometry("300x200")

lb1=Label(root,bg="blue",fg="white",width=21,height=5)
lb2=Label(root,bg="red",fg="white",width=21,height=5)
e1=Entry(root,width=21)
e2=Entry(root,width=21)
bt1=Button(root,width=21,height=5,bg="green",fg="white",text="Player 1",command=py1)
bt2=Button(root,width=21,height=5,bg="green",fg="white",text="Player 2",command=py2)


#grid
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)
e1.grid(row=1,column=0)
e2.grid(row=1,column=1)
bt1.grid(row=2,column=0)
bt2.grid(row=2,column=1)


mainloop()
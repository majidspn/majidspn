from tkinter import*
import time
from datetime import datetime

def tp1():
    ss=0
    s=0
    m=0
    while True:
        r=f"{m}:{s}:{ss}"
        lb1.config(text=r)
        root.update()
        time.sleep(0.01)
        ss+=1
        if ss>99:
            ss=0
            s+=1
        if s>59:
            s=0
            m+=1
def tp2():
    ss=0
    s=0
    m=0
    while True:
        r=f"{m}:{s}:{ss}"
        lb2.config(text=r)
        root.update()
        time.sleep(0.01)
        ss+=1
        if ss>99:
            ss=0
            s+=1
        if s>59:
            s=0
            m+=1

root=Tk()
root.geometry("230x280")
root.title("Game timer")
res=StringVar()
lb1=Label(root,bg="pink",height=4,width=33)
bt1=Button(root,text="start Player 1",bg="blue",fg="white",height=4,width=33,command=tp1)
bt2=Button(root,text="start Player 2",bg="red",fg="white",height=4,width=33,command=tp2)
lb2=Label(root,bg="yellow",height=4,width=33)


lb1.grid()
bt1.grid()
bt2.grid()
lb2.grid()

mainloop()
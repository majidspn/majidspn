from tkinter import*
def upt():
    global tmp
    tmp=tmp+1
    t.set(str(tmp)+" Centigrad")
    global k
    if tmp>=30:
        k.set("Cooler on")
        lb2.config(bg="blue")

def downt():
    global tmp
    tmp=tmp-1
    t.set(str(tmp)+" Centigrad")
    global k
    if tmp<30:
        k.set("Cooler off")
        lb2.config(bg="red")
root=Tk()
root.title("Laptop Cooler")
root.geometry("500x250")
root.config(bg="pink")
tmp=20
t=StringVar()
t.set(str(tmp)+" Centigrad")
k=StringVar()
k.set("Cooler off")
btn1=Button(root,text="UP",bg="green",fg="white",width=35,height=3,command=upt)
btn2=Button(root,text="DOWN",bg="red",fg="white",width=35,height=3,command=downt)
lb1=Label(root,textvariable=t,bg="pink",font=("Arial",20))
lb2=Label(root,textvariable=k,bg="red",fg="white",font=("Arial",20))
btn1.grid(row=0,column=0)
lb1.grid(row=1,column=0,pady=40)
lb2.grid(row=1,column=1,padx=60)
btn2.grid(row=4,column=0,pady=20)
mainloop()
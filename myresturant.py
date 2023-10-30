from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.geometry("330x440")

pizza=0
potato=0
sandwich=0

def incpizza():
    global pizza
    pizza+=1
    reslb.config(text=str(pizza))

def decpizza():
    global pizza
    if pizza>0:
        pizza-=1
    reslb.config(text=str(pizza))

def incpotato():
    global potato
    potato+=1
    reslb1.config(text=str(potato))

def decpotato():
    global potato
    if potato>0:
        potato-=1
    reslb1.config(text=str(potato))

def incsandwich():
    global sandwich
    sandwich+=1
    reslb2.config(text=str(sandwich))

def decsandwich():
    global sandwich
    if sandwich>0:
        sandwich-=1
    reslb2.config(text=str(sandwich))

def order():
    global pizza,potato,sandwich
    

    winres=Toplevel()
    Label(winres,text="food name").grid(row=0,column=0)
    Label(winres,text="number").grid(row=0,column=1)
    Label(winres,text="price").grid(row=0,column=2)
    Label(winres,text="finish price").grid(row=0,column=3)

    rowi=1
    if pizza>0:
        Label(winres,text="PIZZA").grid(row=rowi,column=0)
        Label(winres,text="100$").grid(row=rowi,column=2)
        Label(winres,text=str(pizza)).grid(row=rowi,column=1)
        Label(winres,text=str(pizza*100)+"$").grid(row=rowi,column=3)
        rowi+=1

    if potato>0:
        Label(winres,text="POTATO").grid(row=rowi,column=0)
        Label(winres,text="70$").grid(row=rowi,column=2)
        Label(winres,text=str(potato)).grid(row=rowi,column=1)
        Label(winres,text=str(potato*70)+"$").grid(row=rowi,column=3)
        rowi+=1

    if sandwich>0:
        Label(winres,text="SANDWICH").grid(row=rowi,column=0)
        Label(winres,text="80$").grid(row=rowi,column=2)
        Label(winres,text=str(sandwich)).grid(row=rowi,column=1)
        Label(winres,text=str(sandwich*80)+"$").grid(row=rowi,column=3)
        rowi+=1
    
    Label(winres,text="total="+str((pizza*100)+(potato*70)+(sandwich*80))+"$").grid(row=rowi,column=0)
    


#pizza image and label and inc dec
image=Image.open('4.png')
img=image.resize((150, 130))
my_img=ImageTk.PhotoImage(img)
label=Label(root, image=my_img)
label.grid(row=0, column=0,rowspan=3)

lb=Label(root,text="PIZZA",font=('',16))
lb.grid(row=0,column=1)
lbp=Label(root,text="price:100$",font=('',12))
lbp.grid(row=1,column=1)


plusbt=Button(root,text="+",bg="green",fg="white",width=5,command=incpizza)
plusbt.grid(row=0,column=2)

reslb=Label(root,text=str(pizza),width=5)
reslb.grid(row=1,column=2)

minbt=Button(root,text="-",bg="red",fg="white",width=5,command=decpizza)
minbt.grid(row=2,column=2)

#potato image and label and inc dec
image1=Image.open('5.png')
img1=image1.resize((150, 130))
my_img1=ImageTk.PhotoImage(img1)
label1=Label(root, image=my_img1)
label1.grid(row=3, column=0,rowspan=3)

lb1=Label(root,text="POTATO",font=('',16))
lb1.grid(row=3,column=1)

lbp1=Label(root,text="price:70$",font=('',12))
lbp1.grid(row=4,column=1)

plusbt1=Button(root,text="+",bg="green",fg="white",width=5,command=incpotato)
plusbt1.grid(row=3,column=2)

reslb1=Label(root,text="0",width=5)
reslb1.grid(row=4,column=2)

minbt1=Button(root,text="-",bg="red",fg="white",width=5,command=decpotato)
minbt1.grid(row=5,column=2)

#sandwich image and label and inc dec
image2=Image.open('1.gif')
img2=image2.resize((150, 130))
my_img2=ImageTk.PhotoImage(img2)
label2=Label(root, image=my_img2)
label2.grid(row=6, column=0,rowspan=3)

lb2=Label(root,text="SANDWICH",font=('',16))
lb2.grid(row=6,column=1)

lbp2=Label(root,text="price:80$",font=('',12))
lbp2.grid(row=7,column=1)

plusbt2=Button(root,text="+",bg="green",fg="white",width=5,command=incsandwich)
plusbt2.grid(row=6,column=2)

reslb2=Label(root,text="0",width=5)
reslb2.grid(row=7,column=2)

minbt2=Button(root,text="-",bg="red",fg="white",width=5,command=decsandwich)
minbt2.grid(row=8,column=2)

cancelbtn=Button(root,text="cancel",bg="orange",fg="white",width=20,command=root.destroy)
cancelbtn.grid(row=9,column=0)
orderbtn=Button(root,text="order",bg="blue",fg="white",width=20,command=order)
orderbtn.grid(row=9,column=1,columnspan=2)
mainloop()
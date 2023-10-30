from os import *
names=["ali","reza"]
phones=["0912","0936"]
while True:
    print("1-add\n2-del\n3-print phonebook\n4-search\n5-exit")
    k=int(input("select one of top:"))
    system('cls')
    if k==1:
        name=input("enter name:")
        phone=input("enter phone number:")
        names.append(name)
        phones.append(phone)
    elif k==2:
        name=input("enter name for delete:")
        i=names.index(name)
        names.remove(name)
        phones.pop(i)
    elif k==3:
        for name in names:
            i=names.index(name)
            print(f"{name} {phones[i]}")
    elif k==4:
        print("1-search by name\n2-search by phone")
        b=int(input("select one of top:"))
        if b==1:
            name=input("enter name for search:")
            hlp=0
            for e in names:
                if e==name:
                    hlp=1
                    break
            if hlp==1:
                i=names.index(name)
                print(f"{name} {phones[i]}")
            else:
                print("name doesn't existed")
        if b==2:
            phone=input("enter phone for search:")
            hlp=0
            for e in phones:
                if e==phone:
                    hlp=1
                    break
            if hlp==1:
                i=phones.index(phone)
                print(f"{names[i]} {phones[i]}")
            else:
                print("phone doesn't existed")
    elif k==5:
        break
    print("\n")
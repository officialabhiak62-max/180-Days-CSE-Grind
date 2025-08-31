import random as r
print("WELCOME TO PROJECT")
print("1.Guessing Game pro/n2.ATM Simulator")
a=int(input("Enter the What you want:"))
if a==1:
    e=0
    b=r.randint(1,101)
    while True:
        q=int(input("ENETR YOUR GEUSS"))
        e+=1
        if q>b:
            print("HIGH")
        elif b>q:
            print("LOW") 
        else:
            print("YOU WON ")
            break       
    print("NUMBER OF ATTEMPT")    
if a==2:
    u=1000
    while True:
        print("YOU BALANCE-->1000")
        print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
        g=eval(input("Enter Operation"))
        if g==1 or g=="Deposit":
            x=float(input("ENTER AMOUNT YOU WNT TO DEPOSIT:"))
            u=x+u
        elif g==2 or g=="Withdraw":
            x=float(input("ENTER AMOUNT YOU WNT TO DEPOSIT:"))
            u=u-x
        elif g==3 or g=="Check Balance":
            print("BALANCE :",u)
        else:
            print("BYE")    
            break






















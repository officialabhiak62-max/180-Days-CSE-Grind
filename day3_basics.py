def primeCheck(a):

    if a==2 :
        return "PRIME"

    else:
        for i in range(2,a):
            if a%i==0:
               return "NOT PRIME"
        return "PRIME"              
def u():
    w=[]
    for i in range(2,101):
        p=True
        for j in range(2,i):
             if i%j==0:
              p=False
              break
        if p:
             w.append(i)
    print(w)

a=int(input("enter:"))
print(primeCheck(a))
u()
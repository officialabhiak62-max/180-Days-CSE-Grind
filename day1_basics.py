print("HELLO WORLD")
print("1.Add two number ")
print("2.Find the area to circle")
print("3.Convert to Celsius -->Fahrenheit")
while True:
        c=int(input("ENTER :"))
        try:
            if c==1:
                e=float(input("ENTER NO 1:"))
                r=float(input("ENTER NO 2:"))
                print("ANswer id:",e+r)
        except ValueError:
            print("Please do valid opertaion")        
        try:
            if c==2:
                r=float(input("Enter Radius:"))
                print("Area is :",r*r*3.14159)
        except ValueError:
            print("Please do valid opertaion") 
        try:
            if c==3:
                y=float(input("Enter tempertare:"))
                print("Answer is:",(c*9/5)+32)
        except ValueError:
            print("Please do valid opertaion") 
























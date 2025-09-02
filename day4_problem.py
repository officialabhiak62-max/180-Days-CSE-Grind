'''s,k=input("enter :"),int(input("k :"))
e=
for i in range(0,len(s)+1,k):
    if i==0:
        continue
    for j in range(i-3,i):
        e.append(print(s[j],end=""))
    print()

print(e)
'''
s,k=input("enter :"),int(input("k :"))
for i in range(0,len(s)+1,k):
    p=s[i:i+k]
    y=""
    for j in p:
        if j not in y:
            y+=j
    print(y)  
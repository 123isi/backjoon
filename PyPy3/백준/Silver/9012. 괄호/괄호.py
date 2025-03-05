x=int(input())
for i in range(x):
    c=0
    a=input()
    li=list(a)
    b=[]
    for i in li:
        if i=="(":
            b.append(i)
        elif i==")":
            if len(b)==0:
                c=1
                break
            else:
                b.pop()
    if len(b)==0 and c==0:
        print("YES")
    else:
        print("NO")

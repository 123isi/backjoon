a=int(input())
li=[]
for i in range(a):
    x,y,z=map(int,input().split())
    if x==y==z:
        li.append(x*1000+10000)
    elif x==y:
        li.append(y*100+1000)
    elif x==z:
        li.append(z*100+1000)
    elif z==y:
        li.append(z*100+1000)
    else:
        if x>y and x>z:
            li.append(x*100)
        elif y>z and y>x:
            li.append(y*100)
        else:
            li.append(z*100)
li.sort()
print(li[a-1])

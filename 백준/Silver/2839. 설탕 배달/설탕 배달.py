x=int(input())
a=0
if x%5==0:
    print(x//5)
else:
    while x>0:
        a+=1
        x-=3
        if x%5==0:
            a+=x//5
            print(a)
            break
        elif x==2 or x==1:
            print(-1)
            break
        elif x==0:
            print(a)
            break
import math
a=int(input())
li=list(map(int,input().split()))
b=li[0]
li.remove(b)
for i in range(len(li)):
    c=math.gcd(b,li[i])
    print(b//c,end="")
    print('/',end="")
    print(li[i]//c)
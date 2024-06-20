import math
x=int(input())
li=map(int,input().split())
y=int(input())
arr=map(int,input().split())
a=1
b=1
for i in li:
    a*=i
for i in arr:
    b*=i
c=math.gcd(a,b)
num=list(map(int,str(c)))
d=len(str(c))
result=[]
if d>9:
    result.append(num[-9])
    result.append(num[-8])
    result.append(num[-7])
    result.append(num[-6])
    result.append(num[-5])
    result.append(num[-4])
    result.append(num[-3])
    result.append(num[-2])
    result.append(num[-1])
    print(''.join(str(x) for x in result))
else:
    print(c)
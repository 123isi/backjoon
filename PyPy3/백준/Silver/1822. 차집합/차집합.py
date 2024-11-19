a,b=map(int,input().split())
li=set(map(int,input().split()))
arr=set(map(int,input().split()))
x=li-arr
x=list(x)
x.sort()
y=len(x)
if y==0:
    print(0)
else:
    print(y)
    print(*x)
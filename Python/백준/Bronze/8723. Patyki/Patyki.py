li=list(map(int,input().split()))
li.sort()
a=li[0]
b=li[1]
c=li[2]
if a==b==c:
    print(2)
elif a**2+b**2==c**2:
    print(1)
else:
    print(0)
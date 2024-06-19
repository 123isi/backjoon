a=0
x=int(input())
while x>=0:
    if x>=3:
        x-=3
        a+=1
    else:
        x-=1
        a+=1
if a%2!=0:
    print("CY")
else:
    print("SK")
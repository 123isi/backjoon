import sys
input = sys.stdin.readline

a=int(input())
li=list(map(int,input().split()))
li.sort()

l=0
r=a-1
max1=float('inf')
c=(0,0)

while l<r:
    s=li[l]+li[r]
    if abs(s)<max1:
        max1=abs(s)
        c=(li[l],li[r])
    if s<0:
        l+=1
    else:
        r-=1
print(c[0],c[1])

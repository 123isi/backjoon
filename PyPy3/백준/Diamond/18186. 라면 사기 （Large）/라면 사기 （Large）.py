import sys
input=sys.stdin.readline
a,x,y=map(int,input().split())

li=list(map(int,input().split()))
li=li+[0,0]
r=0
if x>y:
    for i in range(a):
        if li[i+1]>li[i+2]:
            c=min(li[i],li[i+1]-li[i+2])
            li[i]-=c
            li[i+1]-=c
            r+=c*(x+y)
            c=min(li[i],li[i+1],li[i+2])
            li[i]-=c
            li[i+1]-=c
            li[i+2]-=c
            r+=c*(x+y+y)
        else:
            c = min(li[i], min(li[i + 2],li[i + 1]))
            li[i] -= c
            li[i + 1] -= c
            li[i + 2] -= c
            r += c*(x+y+y)
            c=min(li[i], min(li[i + 2] ,li[i + 1]))
            li[i] -= c
            li[i + 1] -= c
            r += c * (x+y)
        r+=li[i]*x
else:
    r=sum(li)*x
print(r)
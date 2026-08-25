a=int(input())

li=list(map(int,input().split()))
li=li+[0,0]
r=0
for i in range(a):
    if li[i+1]>li[i+2]:
        c=min(li[i],li[i+1]-li[i+2])
        li[i]-=c
        li[i+1]-=c
        r+=c*5
        c=min(li[i],li[i+1],li[i+2])
        li[i]-=c
        li[i+1]-=c
        li[i+2]-=c
        r+=c*7
    else:
        c = min(li[i], li[i + 2], li[i + 1])
        li[i] -= c
        li[i + 1] -= c
        li[i + 2] -= c
        r += c * 7
        c=min(li[i], min(li[i + 2] ,li[i + 1]))
        li[i] -= c
        li[i + 1] -= c
        r += c * 5
    r+=li[i]*3
print(r)
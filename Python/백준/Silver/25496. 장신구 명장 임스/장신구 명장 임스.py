x,y=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
a=0
while x<=199 and a<len(li):
    x+=li[a]
    a+=1
print(a)
x,y=map(int,input().split())
li=[]

for i in range(x):
    li.append(i+1)

for i in range(1,y+1):
    a,b=map(int,input().split())
    value=li[a-1]
    li[a-1]=li[b-1]
    li[b-1]=value
for i in li:
    print(i)
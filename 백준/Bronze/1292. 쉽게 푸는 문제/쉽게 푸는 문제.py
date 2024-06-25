x,y=map(int,input().split())
li=[]
for i in range(1000):
    for j in range(i):
        li.append(i)
a=0
for i in range(x-1,y):
    a+=li[i]
print(a)
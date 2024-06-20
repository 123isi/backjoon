x,y=map(int,input().split())
li=[]
for i in range(x):
    li.append(0)
for i in range(y):
    a,b,c=map(int,input().split())
    for j in range(a,b+1):
        li[j-1]=c
for i in li:
    print(i,end=' ')
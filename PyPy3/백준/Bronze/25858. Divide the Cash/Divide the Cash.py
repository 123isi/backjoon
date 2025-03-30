a,b=map(int,input().split())
li=[]
for i in range(a):
    li.append(int(input()))
c=b//sum(li)
for i in li:
    print(i*c)
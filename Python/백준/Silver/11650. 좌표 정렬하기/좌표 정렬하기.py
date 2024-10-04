x=int(input())
li=[]
for i in range(x):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort()
for i in li:
    print(*i)
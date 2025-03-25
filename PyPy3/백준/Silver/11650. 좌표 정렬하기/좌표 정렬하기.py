a=int(input())
li=[]
for i in range(a):
    x,y=map(int,input().split())
    li.append((x,y))
li.sort(key=lambda x:(x[0],x[1]))
for i in li:
    print(*i)
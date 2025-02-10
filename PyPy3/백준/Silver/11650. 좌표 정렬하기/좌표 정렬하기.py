a=int(input())
arr=[]
for i in range(a):
    x,y=map(int,input().split())
    arr.append([x,y])
arr.sort(key=lambda x: (x[0],x[-1]))
for i in arr:
    print(*i)
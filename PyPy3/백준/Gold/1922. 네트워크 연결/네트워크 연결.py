import heapq
a=int(input())
b=int(input())
pa=[-1 for _ in range(a+1)]
def find(x):
    if pa[x] < 0:
        return x
    pa[x] = find(pa[x])
    return pa[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        pa[x] += pa[y]
        pa[y] = x
    else:
        pa[y] += pa[x]
        pa[x] = y

arr=[]
s=0
for i in range(b):
    x,y,z=map(int,input().split())
    heapq.heappush(arr,(z,x,y))
for i in range(b):
    z, x, y = heapq.heappop(arr)
    if find(x) != find(y):
        union(x,y)
        s+=z
print(s)

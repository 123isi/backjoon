import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
a,b=map(int,input().split())
pa=[-1 for _ in range(a+1)]

def find(x):
    if pa[x] < 0:
        return x
    pa[x] = find(pa[x])
    return pa[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root < y_root:
        pa[x_root] += pa[y_root]
        pa[y_root] = x_root
    else:
        pa[y_root] += pa[x_root]
        pa[x_root] = y_root

arr=[]
s=0
ab=0
for i in range(b):
    x,y,z=map(int,input().split())
    arr.append((z,x,y))
arr.sort()
for z,x,y in arr:
    if find(x) != find(y):
        union(x,y)
        s+=z
        ab = max(ab,z)
print(s-ab)

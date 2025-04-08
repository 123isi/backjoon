import math
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
a=int(input())
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

li=[]
s=0
ab=0
for i in range(a):
    x,y=map(float,input().split())
    li.append((x,y))
arr=[]
for i in range(a-1):
    for j in range(i+1,a):
        arr.append((math.sqrt((li[i][0] - li[j][0])**2 + (li[i][1] - li[j][1])**2), i, j))
arr.sort()
for k,i,j in arr:
    if find(i) != find(j):
        union(i,j)
        s+=k
print(f'{s:.2f}')

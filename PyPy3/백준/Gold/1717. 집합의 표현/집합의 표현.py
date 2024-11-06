import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def find(x):
    if li[x]==-1:
        return x
    li[x] = find(li[x])
    return li[x]

def union(x,y):
    if find(x)!=find(y):
        li[find(x)] = find(y)

a,b=map(int,input().split())

li=[-1]*(a+1)

for i in range(b):
    o,n, m = map(int, input().split())

    if o==1:
        if find(m)==find(n):
            print('yes')
        else:
            print('no')
    else:
        union(n, m)


import sys
cnt=0
sys.setrecursionlimit(1000000)

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
    n, m = map(int, input().split())

    if find(m)==find(n):
        print(i+1)
        exit()
    else:
        union(n, m)
print(0)

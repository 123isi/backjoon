import heapq

a, b = map(int, input().split())
pa = [-1 for _ in range(a + 1)]

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

arr = []
sum = 0
s = 0

# 도로 입력 처리
for i in range(b):
    x, y, z = map(int, input().split())
    sum += z
    heapq.heappush(arr, (z, x, y))


us = 0
for i in range(b):
    z, x, y = heapq.heappop(arr)
    if find(x) != find(y):
        union(x, y)
        s += z
        us += 1


re = 0
for i in range(1, a + 1):
    if find(i) == i:
        re += 1

if re > 1: 
    print(-1)
else:
    print(sum - s)

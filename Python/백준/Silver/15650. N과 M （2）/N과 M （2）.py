import copy
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
res = []
r = set()

def dfs(k, depth):
    r.add(k)
    if depth == m - 1 and r not in res:
        # print(r)
        res.append(copy.deepcopy(r))
        r.remove(k)
        return
    for i in range(1, n+1):
        if i in r: continue
        dfs(i, depth + 1)
    r.remove(k)

for i in range(1, n + 1):
    dfs(i, 0)
for i in res:
    print(*i)
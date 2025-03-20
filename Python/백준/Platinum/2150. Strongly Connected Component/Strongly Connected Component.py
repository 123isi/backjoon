import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x, y = map(int, input().split())

arr = [[] for _ in range(x + 1)]
arr2 = [[] for _ in range(x + 1)]

visited = [False] * (x + 1)
visited2 = [False] * (x + 1)
li1 = [[0, i] for i in range(x + 1)]
num = 1

for _ in range(y):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr2[b].append(a)

def dfs(node):
    global num
    visited[node] = True
    for a in arr[node]:
        if not visited[a]:
            dfs(a)
    li1[node][0] = num
    num += 1

def dfs2(node, scc):
    visited2[node] = True
    scc.append(node)
    for a in arr2[node]:
        if not visited2[a]:
            dfs2(a, scc)


for i in range(1, x + 1):
    if not visited[i]:
        dfs(i)

li1.sort(reverse=True)

li = []
for _, node in li1:
    if node == 0:
        continue
    if not visited2[node]:
        scc = []
        dfs2(node, scc)
        li.append(sorted(scc) + [-1])

li.sort()
print(len(li))
for scc in li:
    print(*scc)

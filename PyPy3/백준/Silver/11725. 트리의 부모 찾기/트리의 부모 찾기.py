import sys
sys.setrecursionlimit(10**5)
def dfs_parent(graph, current, parent, parents):
    parents[current] = parent
    for neighbor in graph[current]:
        if neighbor != parent:
            dfs_parent(graph, neighbor, current, parents)

n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (n + 1)
dfs_parent(graph, 1, 0, parents)

for i in range(2, n + 1):
    print(parents[i])

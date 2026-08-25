from collections import deque

def dfs(graph, start, visited):
    visited.append(start)
    for neighbor in sorted(graph[start]):  
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))  
    return visited

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dr = dfs(graph, v, [])
br = bfs(graph, v)

print(' '.join(map(str, dr)))
print(' '.join(map(str, br)))

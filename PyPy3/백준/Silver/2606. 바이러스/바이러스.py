def dfs(value, graph, b):
    b.add(value)
    for neighbor in graph[value]:
        if neighbor not in b:
            dfs(neighbor, graph, b)
n = int(input()) 
m = int(input())  
a = {i: [] for i in range(1, n+1)}
for i in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
b = set() 
dfs(1, a, b)
print(len(b) - 1)

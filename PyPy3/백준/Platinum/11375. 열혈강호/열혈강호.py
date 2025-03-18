def dfs(employee):
    for i in arr[employee]:
        if not visited[i]:
            visited[i] = True
            if s[i] == -1 or dfs(s[i]):
                s[i] = employee
                return True
    return False

a, b = map(int, input().split())
arr = []
for _ in range(a):
    temp = list(map(int, input().split()))
    k = temp[0]
    tasks = temp[1:]
    tasks = [t - 1 for t in tasks]
    arr.append(tasks)

s = [-1] * b
result = 0

for i in range(a):
    visited = [False] * b
    if dfs(i):
        result += 1

print(result)

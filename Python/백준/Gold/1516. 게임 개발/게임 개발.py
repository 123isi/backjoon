from collections import deque

n = int(input())
li = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = [0] * (n + 1)

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        li[i] += 1

def whisang():
    result = time[:]
    q = deque()

    for i in range(1, n + 1):
        if li[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            li[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if li[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])

whisang()

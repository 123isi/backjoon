from collections import deque
x, y = map(int, input().split())
v = [0] * 100001
def bfs(start):
    li = deque()
    li.append(start)
    while li:
        a = li.popleft()
        if a == y:
            return v[a]
        for b in (a - 1, a + 1, a * 2):
            if 0 <= b < 100001 and v[b] == 0:
                v[b] = v[a] + 1
                li.append(b)
print(bfs(x))

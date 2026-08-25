from collections import deque
x, y = map(int, input().split())
v = [-1] * 100001  
c = [0] * 100001   
def bfs(start):
    li = deque()
    li.append(start)
    v[start] = 0   
    c[start] = 1     
    while li:
        a = li.popleft()
        for b in (a - 1, a + 1, a * 2):
            if 0 <= b < 100001:
                if v[b] == -1:
                    v[b] = v[a] + 1
                    c[b] = c[a]
                    li.append(b)
                elif v[b] == v[a] + 1:
                    c[b] += c[a]
    return v[y], c[y]
a, b = bfs(x)
print(a)
print(b)

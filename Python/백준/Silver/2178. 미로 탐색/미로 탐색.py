from collections import deque
a, b = map(int, input().split())
li = []
for i in range(a):
    row = list(map(int, input().strip()))
    li.append(row)
dx = [0, 1, 0, -1] 
dy = [1, 0, -1, 0]
def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < a and 0 <= ny < b and li[nx][ny] == 1:
                li[nx][ny] = li[x][y] + 1  
                queue.append((nx, ny))
    return li[a-1][b-1]  
print(bfs(0, 0))

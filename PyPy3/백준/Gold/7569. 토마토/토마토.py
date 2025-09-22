from collections import deque

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and matrix[nz][nx][ny] == 0:
                matrix[nz][nx][ny] = matrix[z][x][y] + 1
                queue.append((nz, nx, ny))

m, n, h = map(int, input().split())
matrix = []
for i in range(h):
    box = []
    for j in range(n):
        box.append(list(map(int, input().split())))
    matrix.append(box)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 1:
                queue.append((z, x, y))

bfs()

res = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 0:
                print(-1)
                exit(0)
        res = max(res, max(matrix[z][x]))

print(res - 1)

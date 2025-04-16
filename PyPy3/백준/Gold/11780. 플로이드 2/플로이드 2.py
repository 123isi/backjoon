import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
arr = [[INF] * n for _ in range(n)]
li = [[-1] * n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if arr[a][b] > c:
        arr[a][b] = c
        li[a][b] = b

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                li[i][j] = li[i][k]
for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF or i == j:
            print(0)
            continue
        p = [i]
        q = i
        while q != j:
            q = li[q][j]
            p.append(q)
        print(len(p), end=' ')
        for node in p:
            print(node + 1, end=' ')
        print()

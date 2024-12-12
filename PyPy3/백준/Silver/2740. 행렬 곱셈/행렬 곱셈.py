x, y = map(int, input().split())
arr = []
for i in range(x):
    arr.append(list(map(int, input().split())))

a, b = map(int, input().split())
li = []
for i in range(a):
    li.append(list(map(int, input().split())))

re = [[0 for _ in range(b)] for _ in range(x)]

for i in range(x):
    for j in range(b):
        for k in range(y):
            re[i][j] += arr[i][k] * li[k][j]

for i in re:
    print(*i)

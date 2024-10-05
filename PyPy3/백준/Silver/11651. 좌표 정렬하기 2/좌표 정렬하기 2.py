x = int(input())
li = []
for i in range(x):
    a, b = map(int, input().split())
    li.append([a, b])
li.sort(key=lambda y: (y[1],y[0]))
for i in li:
    print(*i)

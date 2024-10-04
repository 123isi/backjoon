x = int(input())
li = []

for i in range(x):
    a, b = input().split()
    li.append([int(a), b])
li.sort(key=lambda x: (x[0]))
for i in li:
    print(*i)
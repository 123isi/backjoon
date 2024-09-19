x, y = map(int, input().split())
li = list(map(int, input().split()))

li.sort()

for i in range(x):
    if li[i] <= y:
        y += 1

print(y)
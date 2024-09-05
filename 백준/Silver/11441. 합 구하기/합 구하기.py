x = int(input())
li = list(map(int, input().split()))
y = int(input())

sumd = [0] * (x + 1)
for i in range(1, x + 1):
    sumd[i] = sumd[i - 1] + li[i - 1]

for _ in range(y):
    a, b = map(int, input().split())
    result = sumd[b] - sumd[a - 1]
    print(result)

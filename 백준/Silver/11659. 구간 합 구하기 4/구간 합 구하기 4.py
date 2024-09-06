import sys
input = sys.stdin.readline

x, y = map(int, input().split())
li = list(map(int, input().split()))

result = [0] * (x + 1)
for i in range(1, x + 1):
    result[i] = result[i - 1] + li[i - 1]

for _ in range(y):
    a, b = map(int, input().split())
    print(result[b] - result[a - 1])

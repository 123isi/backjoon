import sys

input = sys.stdin.read
data = input().split()

x, y = int(data[0]), int(data[1])
li = list(map(int, data[2:]))

a = sum(li[:y])
b = a

for i in range(1, x - y + 1):
    b = b - li[i - 1] + li[i + y - 1] 
    a = max(a, b)

print(a)

import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
d = a % b
for _ in range(c):
    d *= 10
    s = d // b
    d %= b
print(int(s))

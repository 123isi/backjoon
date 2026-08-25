import sys
import math
input = sys.stdin.readline

x = int(input())
li = list(map(int, input().split()))
a = int(input())

b = sum(li)

c = math.comb(b, a)
y = 0
for i in li:
    if i >= a:
        y += math.comb(i, a)

print(y / c)

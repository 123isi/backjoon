import sys
from collections import deque
a = deque()
input = sys.stdin.readline

x,y = map(int, input().split())
b = list(map(int, input().split()))


for i in range(x):

    while a and (a[-1][1] > b[i]):
        a.pop()

    a.append((i + 1, b[i]))

    if a[-1][0] - a[0][0] >= y:
        a.popleft()

    print(a[0][1], end=' ')

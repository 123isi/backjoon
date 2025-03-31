from collections import deque
import sys
input=sys.stdin.readline
li = deque()
x = int(input())

for _ in range(x):
    a = input().strip().split()

    if a[0] == "push":
        li.append(int(a[1]))
    elif a[0] == "front":
        print(li[0] if li else -1)
    elif a[0] == "back":
        print(li[-1] if li else -1)
    elif a[0] == "pop":
        print(li.popleft() if li else -1)
    elif a[0] == "size":
        print(len(li))
    elif a[0] == "empty":
        print(1 if not li else 0)

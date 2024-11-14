import sys
from collections import deque
input = sys.stdin.readline
x = int(input())
q = deque([(x, 0)])
visited = {x} 
while q:
    a, b = q.popleft()
    if a == 1:
        print(b)
        break
    if a % 3 == 0 and (a // 3) not in visited:
        visited.add(a // 3)
        q.append((a // 3, b + 1))
    if a % 2 == 0 and (a // 2) not in visited:
        visited.add(a // 2)
        q.append((a // 2, b + 1))
    if (a - 1) not in visited:
        visited.add(a - 1)
        q.append((a - 1, b + 1))
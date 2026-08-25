import sys
from collections import deque
x=int(sys.stdin.readline())
li=deque()
for i in range(x):
    li.append(i+1)
while len(li)>1:
    li.popleft()
    li.append(li.popleft())
print(li[0])
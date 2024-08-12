import sys

x = int(sys.stdin.readline())
li = set(map(int, sys.stdin.readline().split()))
y = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
for i in arr:
    if i in li:
        print(1)
    else:
        print(0)

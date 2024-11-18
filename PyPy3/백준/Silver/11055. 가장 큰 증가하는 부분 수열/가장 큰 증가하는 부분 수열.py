
import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
arr = li[:]

for i in range(1, n):
    for j in range(i):
        if li[i] > li[j]:
            arr[i] = max(arr[i], arr[j] + li[i])

print(max(arr))

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(map(int, input().split()))

arr = []

def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    a = 0
    for i in range(start,n):
        if a != li[i]:
            arr.append(li[i])
            a = li[i]
            dfs(i )
            arr.pop()

dfs(0)

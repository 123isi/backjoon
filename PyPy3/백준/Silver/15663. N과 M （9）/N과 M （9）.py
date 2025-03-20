import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(map(int, input().split()))

arr = []
visited = [False] * n  

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return

    a = 0
    for i in range(n):
        if not visited[i] and a != li[i]:
            visited[i] = True
            arr.append(li[i])
            a = li[i]
            dfs()
            visited[i] = False
            arr.pop()

dfs()

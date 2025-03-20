import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = sorted(map(int, input().split()))

result = []

def dfs():
    if len(result) == m:
        print(' '.join(map(str, result)))
        return

    for i in range(n):
        if li[i] in result:
            continue
        result.append(li[i])
        dfs()
        result.pop()

dfs()

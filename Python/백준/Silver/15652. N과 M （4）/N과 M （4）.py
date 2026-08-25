import sys

input = sys.stdin.readline

x, y = map(int, input().split())
li = []


def dfs(start):
    if len(li) == y:
        print(' '.join(map(str, li)))
        return

    for i in range(start, x + 1):
        li.append(i)
        dfs(i)
        li.pop()


dfs(1)

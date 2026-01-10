x, y = map(int, input().split())
li = list(map(int, input().split()))
li.sort()

answer = 0

def dfs(n):
    global answer, x, li
    if n > x:
        return
    if n > answer:
        answer =n
    for d in li:
        dfs(n * 10 + d)

dfs(0)
print(answer)

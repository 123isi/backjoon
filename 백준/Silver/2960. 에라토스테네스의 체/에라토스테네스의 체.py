import sys

input = sys.stdin.readline
x, y = map(int, input().strip().split())

li = [False] * (x + 1)
cnt = 0

for i in range(2, x + 1):
    if not li[i]:
        for j in range(i , x + 1, i):
            if not li[j]:

                li[j] = True

                cnt += 1
                if cnt == y:
                    print(j)
                    exit()

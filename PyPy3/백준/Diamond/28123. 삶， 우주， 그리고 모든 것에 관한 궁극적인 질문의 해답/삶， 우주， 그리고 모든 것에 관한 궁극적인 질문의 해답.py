p = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4]

n, k, x = map(int, input().split())

ans = (n + 1 - p[x]) - 3 * (k - 1)
if x in (4, 8, 9):
    ans += 1

print(ans)

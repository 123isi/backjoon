x, y = map(int, input().split())
li = []
for _ in range(0, x):
    li.append(int(input()))
dp = [0] * (y+1)
dp[0] = 1
for i in li:
    for j in range(i, y+1):
        dp[j] = dp[j] + dp[j-i]
print(dp[y])
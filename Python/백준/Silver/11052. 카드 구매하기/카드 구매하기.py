a = int(input())
li = list(map(int, input().split()))
dp = [0] * (a + 1)
for i in range(1, a + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + li[j - 1])

print(dp[a])

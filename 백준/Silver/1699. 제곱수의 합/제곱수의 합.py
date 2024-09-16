x = int(input())

dp = [i for i in range(x+1)]

for i in range(1, x+1):
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i - j*j] + 1)
        j += 1

print(dp[x])
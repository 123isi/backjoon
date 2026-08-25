MOD = 1000000000
x=int(input())
dp = [0] * (x + 1)
dp[0] = 1

twomul = [1]
while twomul[-1] * 2 <= x:
    twomul.append(twomul[-1] * 2)

for i in twomul:
    for j in range(i, x + 1):
        dp[j] = (dp[j] + dp[j - i]) % MOD

print(dp[x])

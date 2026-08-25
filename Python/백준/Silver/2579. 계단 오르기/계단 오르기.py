a = int(input())
li = []
for i in range(a):
    li.append(int(input()))
dp = {}
dp[0] = li[0]
if a > 1:
    dp[1] = li[1] + li[0]
if a > 2:
    dp[2] = max(li[2] + li[0], li[2] + li[1])
for i in range(3, a):
    dp[i] = max(dp[i-2] + li[i], dp[i-3] + li[i] + li[i-1])

print(dp[a-1])

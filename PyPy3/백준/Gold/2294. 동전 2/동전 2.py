dp = [float('inf')] * 10001
dp[0] = 0

a, b = map(int, input().split())
li = []
for _ in range(a):
    li.append(int(input()))

for i in range(1, b + 1):
    for j in li:
        if i - j >= 0 and dp[i - j] != float('inf'):
            dp[i] = min(dp[i], dp[i - j] + 1)

if dp[b] == float('inf'):
    print(-1)
else:
    print(dp[b])

x = int(input())
A = list(map(int, input().split()))
dp = [9999] * x
dp[0] = 0
for i in range(x):
    if dp[i] ==9999:
        continue
    for jump in range(1, A[i] + 1):
        if i + jump < x:
            dp[i + jump] = min(dp[i + jump], dp[i] + 1)
if dp[ - 1] ==9999:
    print(-1)
else:
    print(dp[x - 1])

a=int(input())
for al in range(a):
    x=int(input())
    li = list(map(int,input().split()))
    y=int(input())
    dp = [0] * (y+1)
    dp[0] = 1
    for i in li:
        for j in range(i, y+1):
            dp[j] = dp[j] + dp[j-i]
    print(dp[y])
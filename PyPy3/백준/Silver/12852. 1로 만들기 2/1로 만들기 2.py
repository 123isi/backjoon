n = int(input())
if n==1:
    print(0)
    print(1)

else:
    dp=[[10**9, 0] for i in range(n+3)]
    dp[0][0] = 0
    dp[1][0] = 1
    dp[2][0] = 1
    dp[3][0] = 1
    for i in range(2,n+1):
        if dp[i][0] > dp[i-1][0]+1:
            dp[i][0] = dp[i-1][0]+1
            dp[i][1] = i - 1
        if i%2==0:
            if dp[i][0] > dp[i//2][0]+1:
                dp[i][0] = dp[i//2][0]+1
                dp[i][1] = i // 2
        if i%3==0:
            if dp[i][0] > dp[i//3][0]+1:
                dp[i][0] = dp[i//3][0]+1
                dp[i][1] = i // 3
    print(dp[n][0])
    print(n, end=' ')
    while dp[n][1] != 0:
        print(dp[n][1], end=' ')
        n = dp[n][1]
    print(1)
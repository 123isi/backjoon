a = int(input())
dp = [0] * 10001


dp[0] = 1
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 3
dp[6] = 4
dp[7] = 5
dp[8] = 7
dp[9] = 9


for _ in range(a):
    b = int(input())
    if dp[b] == 0:
        for j in range(10, b + 1):
            dp[j] = dp[j - 2] + dp[j - 3]

    print(dp[b-1])

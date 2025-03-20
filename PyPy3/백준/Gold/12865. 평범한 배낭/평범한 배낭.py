def knapsack(li, arr, W):
    n = len(li)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(W + 1):
            if li[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],dp[i - 1][w - li[i - 1]] + arr[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]
li = []
arr = []

a,b=map(int,input().split())
for i in range(a):
    x,y=map(int,input().split())
    li.append(x)
    arr.append(y)
print(knapsack(li, arr, b))

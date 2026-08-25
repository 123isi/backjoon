dp={}
dp[0]=1
dp[1]=2
dp[2]=4

a=int(input())
for i in range(a):
    b=int(input())
    for j in range(3,b+1):
        dp[j]=dp[j-3]+dp[j-2]+dp[j-1]
    print(dp[b-1])

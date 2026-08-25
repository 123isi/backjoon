a=int(input())
dp=[1000000]*(a+1)
dp[0]=0
for i in range(1,a+1):
    if i>=2:
        dp[i]=dp[i-2]+1
    if i>=5:
        dp[i]=min(dp[i],dp[i-5]+1)
if dp[a]>=1000000:
    print(-1)

else:
    print(dp[a])
x=int(input())
li=list(map(int,input().split()))
dp=[list(li) for _ in range(2)]
vksquf=0
dp[0][0] = li[0]
dp[1][0] = li[0]
for i in range(1,x):
    dp[0][i]=max(dp[0][i-1]+li[i],li[i])
    dp[1][i]=max(dp[0][i-1],dp[1][i-1]+li[i])
print(max(max(dp[0]), max(dp[1])))

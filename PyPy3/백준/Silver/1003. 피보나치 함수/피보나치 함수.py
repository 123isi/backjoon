x=int(input())
li=[]
for i in range(x):
    li.append(int(input()))
a=max(li)
dp=[[0,0] for i in range(a+2)]
dp[0]=[1,0]
dp[1]=[0,1]
for i in range(2,a+1):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
for i in li:
    print(dp[i][0],dp[i][1])

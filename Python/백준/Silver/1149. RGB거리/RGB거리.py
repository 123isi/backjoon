a=int(input())
li=[]
dp=[[0]* 3 for i in range(a)]

for i in range(a):
    x,y,z=map(int,input().split())
    li.append([x,y,z])
dp[0][1]=li[0][1]
dp[0][0]=li[0][0]
dp[0][2]=li[0][2]
for i in range(a):
    dp[i][0]=min(dp[i-1][1]+li[i][0],dp[i-1][2]+li[i][0])
    dp[i][1] = min(dp[i - 1][0] + li[i][1], dp[i - 1][2] + li[i][1])
    dp[i][2] = min(dp[i - 1][0] + li[i][2], dp[i - 1][1] + li[i][2])
print(min(dp[a-1]))
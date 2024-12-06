x=int(input())
dp=[0]*(x+1)
li=[]
for i in range(x):
    li.append(float(input()))
dp[0]=li[0]
for i in range(1,x):
    dp[i]=max(li[i],(dp[i-1]*li[i]))
print(f'{max(dp):.3f}')
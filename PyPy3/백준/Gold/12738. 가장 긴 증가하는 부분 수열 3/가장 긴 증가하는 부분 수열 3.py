from bisect import bisect_left
n = int(input())
li=list(map(int,input().split()))
dp=[]
for i in li:
    x=bisect_left(dp,i)
    if len(dp)==x:
        dp+=[i]
    else:
        dp[x]=i
print(len(dp))
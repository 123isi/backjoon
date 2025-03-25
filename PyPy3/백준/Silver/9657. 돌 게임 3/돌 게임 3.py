a=int(input())
dp=[""]*(a+5)
dp[1]="SK"
dp[2]="CY"
dp[3]="SK"
dp[4]="SK"

for i in range(5, a + 1):
    if dp[i-1]=="CY" or dp[i-3]=="CY" or dp[i-4]=="CY":
        dp[i]="SK"
    else:
        dp[i]="CY"

print(dp[a])

a=int(input())
f=[0]*(a+2)
f[0]=1
f[1]=1

for i in range(2,a+1):
    f[i]=f[i-1]+f[i-2]
print(f[a-1])
a,b,c=map(int,input().split())
a1,b1,c1=map(int,input().split())
cnt=0
cnt+=max(0,a1-a)+max(0,b1-b)+max(0,c1-c)
print(cnt)
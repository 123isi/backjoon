a=int(input())
x,y,z=map(int,input().split())
cnt=0
cnt+=min(a,x)
cnt+=min(a,y)
cnt+=min(a,z)
print(cnt)
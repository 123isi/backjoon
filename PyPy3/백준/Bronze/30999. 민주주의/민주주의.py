a,b=map(int,input().split())
cnt=0
for i in range(a):
    x=input()
    li=list(x)
    y=li.count('O')
    if y>=b/2:
        cnt+=1
print(cnt)
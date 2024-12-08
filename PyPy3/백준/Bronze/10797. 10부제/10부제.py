a=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    if a==i:
        cnt+=1
print(cnt)
a=int(input())
li=list(map(int,input().split()))
b=int(input())
li.sort()
left=0
right=a-1
cnt=0
while left<right:
    if li[left]+li[right]==b:
        cnt+=1
        left+=1
        right-=1
    elif li[left]+li[right]>b:
        right-=1
    else:
        left+=1
print(cnt)
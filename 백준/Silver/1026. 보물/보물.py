x=int(input())
li=list(map(int,input().split()))
arr=list(map(int,input().split()))
li.sort()
arr=sorted(arr,reverse=True)
a=0
for i in range(x):
    a+=arr[i]*li[i]
print(a)
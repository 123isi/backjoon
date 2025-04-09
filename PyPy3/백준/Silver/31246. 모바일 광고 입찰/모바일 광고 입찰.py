a,b=map(int,input().split())
arr=[]
for i in range(a):
    x,y=map(int,input().split())
    arr.append(y-x)
arr.sort()
if arr[b-1]<0:
    print(0)
else:
    print(arr[b-1])
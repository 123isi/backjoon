x,y=map(int,input().split())
re=0
li=list(str(x))
arr=list(str(y))
for i in range(len(li)):
    for j in range(len(arr)):
        re+=int(li[i])*int(arr[j])
print(re)
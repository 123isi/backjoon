x,y=map(int,input().split())
li=list(map(int,input().split()))
li.sort()
arr=[]
for i in range(x):
    for j in range(i+1,x):
        for k in range(j+1,x):
            if li[i]+li[j]+li[k]<=y:
                arr.append(li[i]+li[j]+li[k])
arr.sort()
print(arr[-1])
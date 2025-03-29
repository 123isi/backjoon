a,b=map(int,input().split())
li=[]
arr=[]
for i in range(a):
    li.append(list(map(int,input())))
for i in range(a):
    arr.append(list(map(int,input())))
c=0
if (a<3 or b<3) and li!=arr:
    print(-1)
    exit()
for i in range(a-2):
    for j in range(b-2):
        if li[i][j]!=arr[i][j]:
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if li[k][l]==0:
                        li[k][l]=1
                    else:
                        li[k][l]=0
            c+=1
if li!=arr:
    print(-1)
    exit()
print(c)

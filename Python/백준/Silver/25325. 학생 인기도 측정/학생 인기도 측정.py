
a=int(input())
li=list(input().split())
arr=[]
for i in range(a):
    li2=list(input().split())
    for j in li2:
        arr.append(j)
arr2={}
for i in li:
    cnt=0
    for j in arr:
        if i==j:
            cnt+=1
    arr2[i]=cnt
for i, j in sorted(arr2.items(), key=lambda x: -x[1]):
    print(i, j)
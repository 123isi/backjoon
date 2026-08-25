li={}
x=int(input())
for i in range(x):
    a,b=input().split()
    if a not in li:
        li[a]=True
    else:
        if b=="enter":
            li[a]=True
        else:
            li[a]=False
arr=[]
for i in li.keys():
    if li[i]:
        arr.append(i)
arr.sort(reverse=True)
for i in arr:
    print(i)

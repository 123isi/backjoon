a=int(input())
li=list(str(a))
c=0
arr=[]
if '0' in li:
    for i in li:
        c+=int(i)
        arr.append(int(i))
    if c%3==0:
        arr.sort(reverse=True)
        for i in arr:
            print(i,end="")
    else:
        print(-1)
else:
    print(-1)
a=int(input())
li=list(str(a))
arr=[]
for i in li:
    arr.append(int(i))
arr.sort(reverse=True)
for i in arr:
    print(i,end="")
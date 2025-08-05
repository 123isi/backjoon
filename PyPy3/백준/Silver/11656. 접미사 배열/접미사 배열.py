a=input()
li=list(a)
arr=[]
for i in range(len(li)):
    arr.append(a[i:])
arr.sort()
for i in arr:
    print(i)
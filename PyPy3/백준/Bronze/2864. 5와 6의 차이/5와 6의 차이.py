a,b=map(int,input().split())
li=list(str(a))
arr=list(str(b))
for i in range(len(li)):
    if li[i]=="6":
        li[i]="5"
for i in range(len(arr)):
    if arr[i]=="6":
        arr[i]="5"

c = int(''.join(li))
d = int(''.join(arr))
print(c+d,end=" ")
for i in range(len(li)):
    if li[i]=="5":
        li[i]="6"
for i in range(len(arr)):
    if arr[i]=="5":
        arr[i]="6"

c = int(''.join(li))
d = int(''.join(arr))
print(c+d)

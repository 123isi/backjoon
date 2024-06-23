x,y,z=map(int,input().split())
a=input()
li=list(a)
arr=[x,y,z]
arr.sort()
if li[0]=="A":
    print(arr[0],end=' ')
elif li[0]=="B":
    print(arr[1],end=' ')
elif li[0]=="C":
    print(arr[2],end=' ')
if li[1]=="A":
    print(arr[0],end=' ')
elif li[1]=="B":
    print(arr[1],end=' ')
elif li[1]=="C":
    print(arr[2],end=' ')
if li[2]=="A":
    print(arr[0],end=' ')
elif li[2]=="B":
    print(arr[1],end=' ')
elif li[2]=="C":
    print(arr[2],end=' ')
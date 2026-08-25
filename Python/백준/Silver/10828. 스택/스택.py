a=int(input())
li=[]
arr=[]
for i in range(a):
    li=list(input().split())
    if li[0]=="push":
        arr.append(int(li[1]))
    elif li[0]=="pop":
        if len(arr)==0:
            print(-1)
        else:
           print(arr.pop())

    elif li[0]=="size":
        print(len(arr))
    elif li[0]=="empty":
        if len(arr)==0:
            print("1")
        else:
            print("0")
    elif li[0]=="top":
        if len(arr)==0:
            print("-1")
        else:
            print(arr[-1])
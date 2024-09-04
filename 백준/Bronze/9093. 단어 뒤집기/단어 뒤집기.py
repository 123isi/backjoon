x=int(input())
for i in range(x):
    li=list(input().split())
    for i in li:
        arr=list(i)
        for j in range(len(arr),0,-1):
            print(arr[j-1],end="")
        print(" ",end='')

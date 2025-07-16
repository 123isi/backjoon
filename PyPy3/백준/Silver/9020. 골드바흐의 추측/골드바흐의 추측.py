a=int(input())
li=[]
for i in range(a):
    li.append(int(input()))
b=max(li)
arr=[False]*(b+1)
li1=[]
for i in range(2,b+1):
    if arr[i]==False:
        arr[i]=True
        li1.append(i)
        for j in range(i,b+1,i):
            arr[j]=True
for i in li:
    left = 0
    right = len(li1) - 1
    answer = (0, 0)
    while left <= right:
        s = li1[left] + li1[right]
        if s == i:
            answer = (li1[left], li1[right])
            left += 1
            right -= 1
        elif s < i:
            left += 1
        else:
            right -= 1
    print(*answer)


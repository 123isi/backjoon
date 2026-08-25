from collections import deque
li=deque()
a=int(input())
for i in range(a):
    arr=list(input().split())
    if arr[0]=='back':
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])
    elif arr[0]=='front':
        if len(li)==0:
            print(-1)
        else:
            print(li[0])
    elif arr[0]=='size':
        print(len(li))
    elif arr[0]=='empty':
        if len(li)==0:
            print(1)
        else:
            print(0)
    elif arr[0]=='push_front':
        li.appendleft(arr[1])
    elif arr[0]=='push_back':
        li.append(arr[1])
    elif arr[0]=='pop_front':
        if len(li)==0:
            print(-1)
        else:
            print(li.popleft())
    else:
        if len(li)==0:
            print(-1)
        else:
            print(li.pop())
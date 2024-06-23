x=int(input())
b=0
for i in range(x):
    a=int(input())
    li=list(map(int,input().split()))
    for j in li:
        b+=j
    li.clear()
    print(b)
    b=0
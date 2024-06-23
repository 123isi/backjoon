x=int(input())
a=100000000000000
b=0
for i in range(x):
    li=list(map(int,input().split()))
    for j in li:
        if j%2==0:
            b+=j
            if j<a:
                a=j
    print(b,a)
    li.clear()
    b=0
    a=10000000000000000

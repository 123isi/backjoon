a=int(input())
max=0
for i in range(a):
    x=int(input())
    max=0
    for j in range(x):
        b,y=input().split()
        if max<int(b):
            max=int(b)
            name=y

    print(name)
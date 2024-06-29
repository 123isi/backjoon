x=int(input())
for i in range(x):
    for j in range(i):
        print("*",end="")
    if i!=0:
        print()
for i in range(x,0,-1):
    for j in range(i):
        print("*",end="")
    print()
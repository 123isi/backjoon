a=int(input())
for i in range(a,0,-1):
    for j in range(a-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()
for i in range(2,a+1):
    for j in range(a-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()
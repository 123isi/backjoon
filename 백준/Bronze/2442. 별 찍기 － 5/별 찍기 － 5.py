x=int(input())
for i in range(x-1,0,-1):
    for j in range(i):
        print(" ",end='')
    for k in range((x-i)*2-1):
        print("*",end='')
    print()
for i in range(x*2-1):
    print("*",end='')

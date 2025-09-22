a=3
while a!=0:
    a=int(input())
    if a==0:
        exit()
    for i in range(a):
        for j in range(i+1):
            print("*",end='')
        print()
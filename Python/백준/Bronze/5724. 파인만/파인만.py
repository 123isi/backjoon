a=99
while a!=0:
    a=int(input())
    c=0
    if a==0:
        exit()
    for i in range(1,a+1):
        c+=i*i
    print(c)
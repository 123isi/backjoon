x=int(input())
for i in range(x):
    a = 2015
    b=input()
    li=set(b)
    for j in li:
        a-=ord(j)
    print(a)
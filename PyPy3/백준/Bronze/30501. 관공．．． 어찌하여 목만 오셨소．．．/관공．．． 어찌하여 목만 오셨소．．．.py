a=int(input())
for i in range(a):
    b=input()
    li=list(b)
    if li.count("S")>0:
        print(b)
        exit()
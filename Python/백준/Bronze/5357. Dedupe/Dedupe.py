a=int(input())
for i in range(a):
    b=input()
    li=list(b)
    prev="Q"
    for i in li:
        if i!=prev:
            prev =i
            print(i,end="")
    print()

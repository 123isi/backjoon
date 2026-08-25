a=int(input())
for i in range(a):
    li=list(map(int,input().split()))
    b=li[0]
    c=sum(li[1:])/b
    d=0
    for j in range(b):
        if c<li[j+1]:
            d=d+1
    print(f'{d/b*100:.3f}',end="")
    print("%")
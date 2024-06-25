x=int(input())
c=0
for i in range(1000000):
    a=list(map(int,str(i)))
    b=sum(a)
    if x==i+b:
        c=i
        break
print(c)

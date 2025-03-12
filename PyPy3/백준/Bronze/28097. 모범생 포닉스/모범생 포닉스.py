a=int(input())
li=list(map(int,input().split()))
b=sum(li)
b+=(8*(a-1))
c=b//24
d=b%24
print(c,d)
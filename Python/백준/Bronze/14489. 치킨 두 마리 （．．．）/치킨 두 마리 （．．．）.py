x,y=map(int,input().split())
a=int(input())
a*=2
b=x+y
if b>=a:
    print(b-a)
    exit()
print(b)
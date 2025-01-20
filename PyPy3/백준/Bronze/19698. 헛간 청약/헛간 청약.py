a,b,c,d=map(int,input().split())
b=b//d
c=c//d
b*=c
print(min(a,b))
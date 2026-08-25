a,b=map(int,input().split())
c,d=map(int,input().split())

x=max(a,c-d)
y=min(b,c+d)
if x>y:
    print("IMPOSSIBLE")
else:
    print(y-x+1)
a=int(input())
for i in range(a):
    x,y,z=map(int,input().split())
    print(y+(z-1)*x)
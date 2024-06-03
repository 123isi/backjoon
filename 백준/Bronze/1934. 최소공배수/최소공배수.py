import math
a=int(input())
for i in range(a):
    x,y=map(int,input().split())
    print(math.lcm(x,y))
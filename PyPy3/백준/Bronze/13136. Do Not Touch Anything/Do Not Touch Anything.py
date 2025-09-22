import math

x,y,z=map(int,input().split())
a=math.ceil(x/z)
b=math.ceil(y/z)
print(a*b)
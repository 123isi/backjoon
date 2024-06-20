import math
x,y=map(int,input().split())
a=math.factorial(x)
b=math.factorial(x-y)
c=math.factorial(y)
print(f'{a/(b*c):.0f}')
import math
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    print(math.lcm(a,b),math.gcd(a,b))
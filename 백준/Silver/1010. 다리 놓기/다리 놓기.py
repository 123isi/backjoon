import math

x=int(input())

for _ in range(x):
    y,z=map(int,input().split())
    br = math.factorial(z) // (math.factorial(y) * math.factorial(z-y))
    print(br)

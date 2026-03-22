import sys
import math
sys=sys.stdin.readline
x, y, z = map(int, input().split())
z-=x
print(1+math.ceil(z/(x-y)))
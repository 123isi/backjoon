import sys
import math
x=int(input())

for i in range(x):
    li=list(map(int, sys.stdin.readline().split()))
    a=0
    for j in range(1,len(li)):
        for k in range(j+1,len(li)):
            a+=math.gcd(li[j],li[k])

    print(a)

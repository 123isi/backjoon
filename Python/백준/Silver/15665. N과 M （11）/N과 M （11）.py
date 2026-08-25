import itertools
from itertools import repeat

a, b = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
arr=[]
for i in itertools.product(li, repeat=b):
    arr.append(i)
arr=set(arr)
arr=list(arr)
arr.sort()
for i in arr:
    print(*i)
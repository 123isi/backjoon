import itertools
from itertools import repeat

a, b = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in itertools.combinations_with_replacement(li, b):
    print(*i)
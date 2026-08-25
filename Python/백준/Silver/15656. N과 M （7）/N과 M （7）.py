import itertools
a, b = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in itertools.product(li,repeat=b):
    print(*i)

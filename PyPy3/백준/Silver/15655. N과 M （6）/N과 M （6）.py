import itertools
a, b = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
for i in itertools.combinations(li,b):
    print(*i)

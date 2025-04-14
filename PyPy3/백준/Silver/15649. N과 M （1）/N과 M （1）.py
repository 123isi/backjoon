import itertools
a, b = map(int, input().split())
for i in itertools.permutations(range(1, a + 1), b):
    print(*i)

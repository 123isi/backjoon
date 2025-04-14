import itertools

a, b = map(int, input().split())

for i in itertools.product(range(1, a + 1), repeat=b):
    print(*i)

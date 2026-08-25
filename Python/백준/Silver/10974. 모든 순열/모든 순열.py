from itertools import permutations

a = int(input())
li = [i + 1 for i in range(a)]
for cwr in permutations(li, a):
    print(*cwr)

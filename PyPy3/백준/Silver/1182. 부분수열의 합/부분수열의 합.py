a, b = map(int, input().split())
li = list(map(int, input().split()))
r = 0

for i in range(1, 2 ** a):
    sum1 = 0
    for j in range(a):
        if i & (2 ** j):
            sum1 += li[j]
    if sum1 == b:
        r += 1

print(r)
